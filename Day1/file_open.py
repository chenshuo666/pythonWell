#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import sys,time
f = open('ali.txt','r',encoding='utf-8')#文件句柄
#a=append 追加
#for line in f.readlines():
    #print(line.strip())#delete space and next line

'''
for  index,line in enumerate(f.readlines()):
    if index== 10:
        print('===============')
        continue
    print(line.strip())
'''
print(f.read())
f.seek(0)#文件指针光标移动到初始位置

print('------------')
print(f.read())
print(f.encoding)
print(f.fileno())#操作系统文件操作接口
print(f.name)#文件名称
print(f.isatty())#是否和终端机（打印机之类）交互
print(f.seekable())#判断光标是否可以移动
print(f.flush())#实时刷新写到硬盘上
#print(f.truncate())#从头阶段字符

'''
for i in range(20):#打印进度条
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)
'''