#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/29 21:22'


f = open('demo.wav', 'rb')

info = f.read(44)

from struct import unpack

# res = unpack('h', info[22:24])  # 通道数，单声道为1，双声道为2
# print res
#
# res = unpack('i', info[24:28])  # 采样频率
# print res

res = unpack('h', info[32:34])  # DATA数据块长度，字节。
print res

res = unpack('h', info[34:36])  # 编码宽度 , PCM位宽
print res

# t = unpack('h', '\x01\x02')
# print t
# t = unpack('>h', '\x01\x02')
# print t


import array

f.seek(0, 2)
print f.tell()

n = (f.tell() - 44)
print n

buf = array.array('h', (0 for _ in xrange(n)))

f.seek(44)

f.readinto(buf)

for i in n:
    buf[i] /= 8

f2 = open('demo2.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()


#
# for x in f.readlines():
#     print x



