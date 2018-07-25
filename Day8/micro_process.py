#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import gevent
from greenlet import greenlet

def test1():
    print("test1")
    gr2.switch()
    print("after test1")
    gr2.switch()


def test2():
    print("test2")
    gr1.switch()
    print("after test2")


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()