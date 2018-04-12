#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 12:20'


class Rectangle(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h