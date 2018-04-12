#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 14:54'

from random import randint

chinese = [range(60, 100) for _ in range(40)]
math = [range(60, 100) for _ in range(40)]
english = [range(60, 100) for _ in range(40)]

# for i in xrange(len(math)):
#     chinese[i] + math[i] + english[i]

# print zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'), [1, 2, 3])
# print zip(chinese, math, english)
print zip([1, 2, 3, 4], (4, 4, 3, 2), [1, 2, 3, 5])

total = []
# for c, m, e in zip(chinese, math, english):
for c, m, e in zip([1, 2, 3, 4], (4, 4, 3, 2), [1, 2, 3, 5]):
    total.append(c + m + e)
print total

from itertools import chain

e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(42)]
e3 = [randint(60, 100) for _ in xrange(42)]
e4 = [randint(60, 100) for _ in xrange(39)]
count = 0

for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1
print count



