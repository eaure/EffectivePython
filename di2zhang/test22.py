#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 11:54'


# # 方法一
# NAME, AGE, SEX, EMAIL = xrange(4)
#
#
# student = ('hackfun', 16, 'male', '1@1.com')
#
# print student[NAME]


# # 方法二
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])  # 类的工厂

s = Student('hackfun', 16, 'male', '1@1.com')

print s.name

s = Student(name='hackfun1', age=17, sex='female', email='2@2.com')
print s.name