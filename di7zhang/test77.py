#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 12:03'

import sys


class A(object):
    def __del__(self):
        print 'in A.__del__'

a = A()

# print sys.getrefcount(a) - 1  # 1
#
# a2 = a
# print sys.getrefcount(a) - 1  # 2
# del a2
# print sys.getrefcount(a) - 1  # 1


# import weakref
#
# print sys.getrefcount(a) - 1
# a_wref = weakref.ref(a)
#
# a2 = a_wref()
# print sys.getrefcount(a) - 1
#
# print a is a2  # True
# print sys.getrefcount(a) - 1  # 2
# del a
# del a2
# print a_wref()  # None
#
# print '------end------'

import weakref

class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return '%s s data, value is %s' % (self.owner(), self.value)

    def __del__(self):
        print 'in Data.__del__'


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print 'in Node.__del'


node = Node(100)
del node
# import gc
# gc.collect()
raw_input('wait...')
