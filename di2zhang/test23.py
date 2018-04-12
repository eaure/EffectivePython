#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 12:07'


from random import randint


# data = [randint(0, 20) for _ in xrange(30)]
#
# print data
#
# c = dict.fromkeys(data, 0)
#
# print c
#
# for x in data:
#     c[x] += 1
#
# print c


from collections import Counter
#
# data = [randint(0, 20) for _ in xrange(30)]
# cnt = Counter(data)
#
# print cnt
# print cnt.most_common(3)


import re

txt = open('linux-kernel-coding-style').read()

c3 = Counter(re.split('\W+', txt))
# print c3
print c3.most_common(10)

















