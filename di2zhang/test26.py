#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:26'


from random import randint
from collections import OrderedDict
from time import time


# d = OrderedDict()
#
# d['Jim'] = (1, 35)
# d['Leo'] = (2, 37)
# d['Bob'] = (3, 40)
#
# for k in d:
#     print d[k]

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start
    d[p] = (i + 1, end - start)

print
print '-' * 20


for k in d:
    print d[k]

