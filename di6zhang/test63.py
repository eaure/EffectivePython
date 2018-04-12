#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 21:47'


from xml.etree.ElementTree import parse


f = open('web.xml')

et = parse(f)

root = et.getroot()
print root.tag
print root.attrib
print root.text
# print root.text.strip()

# for child in root:
#     # print child.get('name')  # 取元素的属性

print root.find('.//servlet')

# for e in root.iterfind('country'):
#     print e.get('name')
#
# list(root.iter())


from xml.etree.ElementTree import iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)

            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass



