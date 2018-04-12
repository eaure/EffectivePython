#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 13:57'

import csv
from xml.etree.ElementTree import Element, ElementTree
from threading import Thread, Event
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
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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
        count = 0
        while True:
            sid, data = self.queue.get()
            print 'Convert', sid
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()

                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0


import tarfile
import os


class TarThead(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')  # w:gz  w代表写，gz代表压缩算法
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)

        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()


if __name__ == '__main__':

    q = Queue()
    dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]

    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q, cEvent, tEvent)
    tThread = TarThead(cEvent, tEvent)
    tThread.start()

    for t in dThreads:
        t.start()

    cThread.start()

    for t in dThreads:
        t.join()

    q.put((-1, None))
