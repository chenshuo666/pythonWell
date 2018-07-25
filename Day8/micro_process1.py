#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import gevent


# def func1():
#     print('\033[31;1mfunc1\033[0m')
#     gevent.sleep(2)
#     print('\033[31;1mafter func1\033[0m')
#
#
# def func2():
#     print('\033[36;1mfunc2\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1mafter func2\033[0m')
#
#
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
#     # gevent.spawn(func3),
# ])

from gevent import monkey

monkey.patch_all()
import gevent
from  urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])