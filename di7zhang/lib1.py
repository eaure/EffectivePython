#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 12:20'


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14
