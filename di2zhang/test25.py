#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:14'

from random import randint, sample


print sample('abcdefg', randint(3, 6))


s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print 's1: ', s1
print 's2: ', s2
print 's3: ', s3

# # 方法一
# res = []
#
# for k in s1:
#     if k in s2 and k in s3:
#         res.append(k)
# print res

# 方法二
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

# 方法三
# print map(dict.viewkeys, [s1, s2, s3])
print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))








