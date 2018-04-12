#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 14:12'


import tarfile
import os


def tarXML(tfname):
    tf = tarfile.open(tfname, 'w:gz')  # w:gz  w代表写，gz代表压缩算法
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)

    tf.close()

    if not tf.members:
        os.remove(tfname)

if __name__ == '__main__':
    tarXML('test.tgz')