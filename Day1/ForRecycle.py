#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
from new_dir import Login
import  sys
import os
for i in range(0,100,2):
    print('Loop:',i)

print(sys.argv)
#print(sys.argv[2])

com=os.popen("dir").read()
print(com)
os.mkdir("new_dir")#创建一个新的文件夹