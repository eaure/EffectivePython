#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/30 7:41'

import sys

x = type("", (), {"__lt__": lambda a, b: True})()


class A(object):

    def __init__(self, a):
        self.a = a

    def __lt__(self, b):
        print 1111
        return self.a < b.a

    def __gt__(self, b):
        print 2222
        return self.a > b.a

# a = A(1)
# b = A(2)


def __init__(self, a):
    self.a = a


def __lt__(self, b):
    return self.a < b


# a, b, c = {0}, {1}, {2}
# print min(b, a, c)
# print min(a, b, c)
# print min(c, a, b)
# # print dir(a)
# print min(b, a) == min(a, b)  # False
# # print x < x


# x, s = True, {1}
# s.add(x)
# print dir(s)
# # print dir(list)
# print map(type, s)
# print s
# print type(x) in map(type, s)  # False


# x, y = [], [0]
# print x < y and all(a >= b for a, b in zip(x, y))  # True


# from collections import Iterator
#
# x, y = type('', (Iterator,), {"__mul__": lambda a, b: [b+1], "next": lambda a: a})(), 1
# print x.__mul__(0)
# # print x * 0
# # print sum(x * 0, y)
# print sum(x * 0, y) == y  # False


# x = [[0]]
# # x = set([[0], [1]])  # 报错, TypeError: unhashable type: 'list'
# print min(*x)
# print min(x)
# print min(x) == min(*x)  # False


# x, y, z = [1], -1, -1
# print x * y
# print y * x
# print x * 3
# print 2 * x
# print x * (y * z)
# print (x * y) * z
# print x * (y * z) == (x * y) * z  # False


# # test_local
# i = 1
# print(i)  # 1
#
# x = [i for i in range(5)]
#
# print(i)  # 4


# x, y = "aa", "aa"
# print "a" > 97  # True
# print max(x)  # True
# print y > max(x)  # True
# print y in x  # True
# print y > max(x) and y in x  # True

# # This snippet is impossible.
# x, y = ???
# print any(x) and not any(x + y)  # True


# x, y = "a", ""
# print len(x)  # 1
# print x.count(y)  # 2
# # print x.replace(y, "c")  # cac
# print x.count(y) <= len(x)  # False


# # No. This snippet is impossible.
# x = [0]
# print all(filter(None, x))  # False


# # No. This snippet is impossible.
# x, a, b, c = "aaaa", 0, 3, 2
# print max(x)
# print max(x[a:b:c])
# print max(x) < max(x[a:b:c])  # True















