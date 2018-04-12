#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 22:49'


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


p1 = Player('0001', 'HackFun')

p2 = Player2('0002', 'HackFun2')

print set(dir(p1)) - set(dir(p2))  # set(['__dict__', '__weakref__'])

import sys
print sys.getsizeof(p1.__dict__)
print sys.getsizeof(p2.__slots__)



