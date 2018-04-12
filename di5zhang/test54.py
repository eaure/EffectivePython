#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 16:13'


import mmap

import array

# s = array.array('i', (0 for _ in range(1024)))
# s = array.array('i', (0 for _ in range(2)))
#
#
# f = open('demo2.bin', 'wb')
# s.tofile(f)
# f.close()

# f = open('demo.bin', 'r+b')

# f.fileno()  # 文件描述符
#
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
#
# print mmap.PAGESIZE
#
# # print type(m)
# #
# # print m[0]
#
# # m[10:20] = '\x88'
# #
# # m[4:8] = 'xff' * 4
# #
# # m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 8, access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE * 4)
#  第二个参数是映射区域的长度,0为全部文件
# # m[:0x1000] = '\xaa' * 0x1000
# m.close()
# f.close()

