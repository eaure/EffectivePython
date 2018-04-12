#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:36'

from random import randint
from collections import deque


history_list = deque([], 5)

N = randint(0, 100)


def guess(k):
    if k == N:
        print 'right'
        return True

    if k < N:
        print "%s is less-than N" % k
    else:
        print "%s is greater-than N" % k

    return False

while True:
    line = raw_input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history_list.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history_list)
    elif line == 'exit':
        break














