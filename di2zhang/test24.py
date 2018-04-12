#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:06'

from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}

# print list(iter(d))  # ['a', 'c', 'b', 'y', 'x', 'z']

# print sorted(d)

# print (97, 'a') > (69, 'b')  # True
# print (97, 'a') > (97, 'b')  # False

# d.keys()
# d.values()
print sorted(zip(d.itervalues(), d.iterkeys()))

print sorted(d.iteritems(), key=lambda x: x[1], reverse=True)
