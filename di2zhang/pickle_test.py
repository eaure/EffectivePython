#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:45'

import pickle
from collections import deque

q = deque([3, 4, 5, 6, 7], 5)

pickle.dump(q, open('history', 'w'))

q2 = pickle.load(open('history'))

print q2
