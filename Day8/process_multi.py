#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import multiprocessing,threading
from multiprocessing import Pipe
import time
#
# def thread_id():
#     print("当前的线程ID是:",threading.get_ident())
#
# def clock(interval):
#     while True:
#         print("the time is %s "%time.ctime())
#         time.sleep(interval)
#         t=threading.Thread(target=thread_id,)
#         t.start()
#
#
# if __name__=="__main__":
#     p=multiprocessing.Process(target=clock,args=(1,))
#     p.start()
#     print(p.name)
#     print(p.is_alive())

def run(conn):
    conn.send("kkk")
    conn.close()


if __name__=="__main__":
    t=1