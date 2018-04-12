#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 14:46'

from itertools import islice

l = range(20)

t = iter(l)

for x in islice(t, 5, 10):  # 他会消耗原来的对象
    print x

print '-' * 30

for x in t:
    print x
