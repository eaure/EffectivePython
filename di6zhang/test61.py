#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 19:44'


# from urllib import urlretrieve
#
# urlretrieve('http://hq.sinajs.cn/list=sh601006', 'pingan.csv')

# import csv
#
# rf = open('pingan.csv', 'rb')
#
# reader = csv.reader(rf)
#
# # print reader.next()
#
# wf = open('pingan_copy.csv', 'wb')
#
# writer = csv.writer(wf)
#
# writer.writerow(reader.next())
# wf.flush()


import csv

with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)

print 'end'

