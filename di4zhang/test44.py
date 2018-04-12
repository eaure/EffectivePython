#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 21:55'

pl = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "500.0"]


l = ['abc', 123, 45, 'xyz']
''.join([str(x) for x in l])  # 列表生成式
''.join((str(x) for x in l))  # 生成器表达式

