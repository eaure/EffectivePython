#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 14:18'


from threading import Event, Thread
from time import sleep


def f(e):
    print 'f 0'
    e.wait()
    print 'f 1'

e =Event()

t = Thread(target=f, args=(e, ))

t.start()

print
print '-' * 20
# sleep(1)
e.set()

# e.clear()
