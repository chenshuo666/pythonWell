#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import pickle
f=open("test.txt",'rb')
def sayhi(name):
    print("hello,",name)
data=pickle.loads(f.read())

print(data)
print(data["func"]("chenshuo"))