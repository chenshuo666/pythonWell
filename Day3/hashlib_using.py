#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import hashlib

m=hashlib.md5()
m.update(b'Hello')
print(m.digest())
print(m.hexdigest())

m1=hashlib.sha512()
m1.update(b'Hello')
print(m1.digest())
print(m1.hexdigest())