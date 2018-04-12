#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/29 20:57'

import re
import sys

s = '\tabc\t123\txyz'

t = s.strip()

s = '---abc+++'

t = s.strip('+-')



s = '\tabc\t123\txyz'

t = s.replace('\t', '')
print t

s = '\tabc\t123\txyz\r'

t = re.sub('[\t\r]', '', s)

print t
# print t,

# sys.stdout.write('ss' + '\n')


s = 'abc1230323xyz'

import string

t = s.translate(string.maketrans('abcxyz', 'xyzabc'))

print t




