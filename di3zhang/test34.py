#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 14:39'


l = [1, 2, 3, 4, 5]

# l.reverse()  # 1
# l[::-1]
# reversed(l)

# for x in reversed(l):
#     print x


class FloatRang():
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for x in iter(FloatRang(1.0, 4.0, 0.5)):
    print x

print '-' * 20


for x in reversed(FloatRang(1.0, 4.0, 0.5)):
    print x
