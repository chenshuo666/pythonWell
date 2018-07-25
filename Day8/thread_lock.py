#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import time
import threading

lock=threading.RLock()
num=0
def run(n):
    lock.acquire()

    global num
    num+=1
    lock.release()

t_obj=[]

for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True) #将当前线程设置成守护线程
    t.start()
    t_obj.append(t)

for t in t_obj:
     t.join()

print("num:",num)