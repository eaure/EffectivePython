#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/28 13:52'

import requests
from collections import Iterable, Iterator

# def getWeather(self, city):
#     r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#     data = r.json()['data']['forecast'][0]
#     return '%s: %s , %s' % (city, data['low'], data['high'])

# [u'北京', u'上海', u'广州', u'长春']
#
# print getWeather(u'北京')
# print getWeather(u'长春')


from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春']):
    print x






