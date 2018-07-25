#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import queue
# q=queue.Queue()
#
# q.put("d1")
# q.put("d2")
# q.put("d3")
# q.get()
# print(q.qsize())

q=queue.PriorityQueue()
q.put(12,'sd')
q.put(32,'fdes')
q.put(89,'fd')
q.put(35,'gufe')

print(q.get())
print(q.get())
print(q.get())
print(q.get())