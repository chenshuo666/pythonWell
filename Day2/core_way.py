#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import pickle

def sayhi(name):
    print("hello,",name)

info={
    'name':"chenshuo",
    "age":22,
    'func':sayhi
}

f=open("test.txt",'wb')
f.write(pickle.dumps(info))
print(type(pickle.dumps(info)))
f.close()
