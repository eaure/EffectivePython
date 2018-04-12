#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 22:03'


# from xml.etree.ElementTree import Element, ElementTree
#
# e = Element('Data')
#
# print e.tag
#
# e.set('name', 'abc')
#
# from xml.etree.ElementTree import tostring
#
# tostring(e)
#
# e.text = '123'
#
# # print tostring(e)
#
# e2 = Element('Row')
# e3 = Element('Open')
#
# e3.text = '8.80'
# e2.append(e3)
#
# print tostring(e2)
#
# e.text = None
#
# e.append(e2)
#
# print tostring(e)
#
#
# et = ElementTree(e)
#
# et.write('demo.xml')


from xml.etree.ElementTree import Element, ElementTree


import csv
from xml.etree.ElementTree import tostring


def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

        return ElementTree


et = csvToXml()












