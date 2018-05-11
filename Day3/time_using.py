#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import time
import datetime
print('1 {}'.format(time.time()))#时间戳
print('2 {}'.format(time.localtime()))#结构化时间
print('3 {}'.format(time.gmtime()))#格林尼治时间
print('4 {}'.format(time.mktime(time.localtime())))#结构化时间转时间戳
print('5 {}'.format(time.strftime('%Y-%m-%d %X',time.localtime())))#结构化时间转字符串时间
print('6 {}'.format(time.strptime('2017-05-12 10:58:36','%Y-%m-%d %X')))#字符串时间转结构化时间
print('7 {}'.format(time.asctime()))#结构化时间转标准字符串显示
print('8 {}'.format(time.ctime()))#时间戳转标准字符显示
print('9 {}'.format(datetime.datetime.now()))