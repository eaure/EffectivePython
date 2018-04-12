#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 23:26'

from functools import total_ordering
from abc import ABCMeta, abstractmethod


@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        print 'in __lt__'
        if not isinstance(other, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < other.area()

    def __eq__(self, other):
        print 'in __eq__'
        return self.area() == other.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14

r1 = Rectangle(5, 3)
r2 = Rectangle(5, 3)
c1 = Circle(3)

print c1 <= r1  # c1.__lt__(r1)
print r1 > c1  # r1.__gt__(c1)
print r1 < r2


