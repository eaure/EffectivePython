#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 15:42'


f = open('demo.txt', 'w')

f.write('abc')

f.write('+' * 4093)  # 默认缓冲区的大小4096

f.write('-')


f = open('demo2.txt', 'w', buffering=2048)  # 0无缓冲，1行缓冲，>1的n，为n缓冲


