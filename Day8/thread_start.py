#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import threading
import time
def run(n):
    print("task",n )
    print(threading.current_thread())
    time.sleep(2)
start_time=time.time()
t_obj=[]

for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True) #将当前线程设置成守护线程
    t.start()
    t_obj.append(t)

# for t in t_obj:
#     t.join()


print("all threads has finished.....",threading.current_thread(),threading.activeCount())
print("cost:",time.time()-start_time)
