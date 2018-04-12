#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 11:52'


class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        # print 'in __get__', instance, owner
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print 'in __set__'
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print 'in __del__'
        del instance.__dict__[self.name]


class A(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

a = A()
a.x = 5
print a.__dict__

a.age = '19'  # TypeError: expected an <type 'int'>

