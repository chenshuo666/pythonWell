#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import threading,time

import queue

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("%s生产了骨头"% name,count )
        count +=1
        time.sleep(2)



def  Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(1)



p = threading.Thread(target=Producer,args=("gg",))
c = threading.Thread(target=Consumer,args=("lala",))
c1 = threading.Thread(target=Consumer,args=("jj",))


p.start()
c.start()
c1.start()
