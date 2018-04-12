#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 12:59'

import csv
from xml.etree.ElementTree import Element, ElementTree
from StringIO import StringIO
import requests
from xml_pretty import pretty

def download(url):
    response = requests.get(url, timeout=1)
    if response.ok:
        print response.content
        return StringIO(response.content)


def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    # headers = reader.next()
    headers = ['8.840', '8.850', '8.750', '8.870', '8.720', '8.750', '8.760', '36195855', '317813401.000', '5400', '8.750', '601284', '8.740', '240500', '8.730', '179100', '8.720', '232000', '8.710', '123100', '8.760', '171778', '8.770', '323300', '8.780', '218500', '8.790', '494025', '8.800', '2017-09-29', '15:00:00', '00']
    print headers
    headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text.decode('gbk').encode('utf8')
            eRow.append(e)

    pretty(root)
    et = ElementTree(root)
    et.write(fxml)


def handle(sid):
    print 'Download...(%d)' % sid
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None:
        return

    pretty('Convert to XML...(%d)') % sid
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)


from threading import Thread


class MyThread(Thread):

    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)


if __name__ == '__main__':
    '''
    url = 'http://hq.sinajs.cn/list=sh601006'
    rf = download(url)
    if rf:
        with open('000001.xml', 'wb') as wf:
            csvToXml(rf, wf)
    '''

    """
    for i in xrange(1, 11):
        t = Thread(target=handle, args=(1, ))
        t.start()
    """

    threads = []
    for i in xrange(1, 11):
        t = MyThread(1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print 'main thread'






