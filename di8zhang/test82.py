#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 13:57'

import csv
from xml.etree.ElementTree import Element, ElementTree
from threading import Thread
import requests
from StringIO import StringIO
from xml_pretty import pretty


from Queue import Queue


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self, url):
        response = requests.get(url, timeout=1)
        if response.ok:
            print response.content
            return StringIO(response.content)

    def run(self):
        print 'Download', self.sid
        # 1.
        data = self.download(self.url)
        # 2. (sid,data)
        self.queue.put((self.sid, data))


class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self, scsv, fxml):
        reader = csv.reader(scsv)
        # headers = reader.next()
        headers = ['8.840', '8.850', '8.750', '8.870', '8.720', '8.750', '8.760', '36195855', '317813401.000', '5400',
                   '8.750', '601284', '8.740', '240500', '8.730', '179100', '8.720', '232000', '8.710', '123100',
                   '8.760', '171778', '8.770', '323300', '8.780', '218500', '8.790', '494025', '8.800', '2017-09-29',
                   '15:00:00', '00']
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

    def run(self):
        while True:
            sid, data = self.queue.get()
            print 'Convert', sid
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)

q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q)

for t in dThreads:
    t.start()

cThread.start()

for t in dThreads:
    t.join()

q.put((-1, None))
