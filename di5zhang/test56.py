#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/2 19:20'


from tempfile import TemporaryFile, NamedTemporaryFile


f = TemporaryFile()

f.write("abcef" * 100000)

f.seek(0)

f.read(100)


ntf = NamedTemporaryFile()

ntf = NamedTemporaryFile(delete=False)

print ntf.name
