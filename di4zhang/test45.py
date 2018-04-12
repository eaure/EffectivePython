#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 22:01'

# s = 'abc'
# print dir(s)
#
# t = s.ljust(20, '=')
# print t
#
# t = s.rjust(20, '=')
# print t
#
# t = s.center(20, '=')
# print t
#
#
# t = format(s, '<20')
# print t
# t = format(s, '>20')
# print t
# t = format(s, '^20')
# print t

d = {'DisCull': 500.0,
     'SmallCull': 0.04,
     'farclip': 477,
     'lodDist': 100.0,
     'trilinear': 40}
x = map(len, d.keys())
print x

w = max(x)
for k in d:
    print k.ljust(w), ':', d[k]