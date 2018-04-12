#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 21:01'

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

res = s.split(';')

# map(lambda x: x.split('|'), res)
# t = []
# map(lambda x: t.extend(x.split('|')), res)
# print t
# t = []
# map(lambda x: t.extend(x.split(',')), t)
# print t

# 方法一
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [x for x in res if x]

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
res = mySplit(s, ';,.|\t')
print res

# 方法二
import re
res = re.split(r'[,;.|\t]+', s)
print res
