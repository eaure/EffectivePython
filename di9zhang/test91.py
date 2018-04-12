#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/10/3 19:55'


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(50)


# def fibonacci(n, cache=None):
#     if cache is None:
#         cache = {}
#
#     if n in cache:
#         return cache[n]
#
#     if n <= 1:
#         return 1
#
#     cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
#     return cache[n]
