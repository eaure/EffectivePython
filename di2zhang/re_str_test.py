#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 12:59'


import re


# str = 'a asd  asd\t\taaa'
#
# s = re.split("\t+| +", str)
# i = 1
# for x in s:
#     print x

str = 'a asd  asd\t\taaa'
s = str.split()
i = 1
for x in s:
    print x

# str = 'hackfun123'
#
# s = re.split("((hackfun|hack)123)", str)
#
# print s
#
#
# s = re.match("((hackfun|hack)123)", str)
# if s:
#     print s.group(2)