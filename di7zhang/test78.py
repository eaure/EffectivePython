#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 12:19'


from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle
from operator import methodcaller


def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        # f = getattr(shape, name, None)
        # if f:
        #     return f()
        if hasattr(shape, name):
            f = methodcaller(name)
            return f(shape)


shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(4, 5)

shapes = [shape1, shape2, shape3]
print map(getArea, shapes)  # [12.56, 6.0, 20]


# from operator import methodcaller
#
# s = 'abc123abc456'
# print s.find('abc', 4)
#
# f = methodcaller('find', 'abc', 4)
# print f(s)


