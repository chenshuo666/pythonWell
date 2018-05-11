#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import socket

client=socket.socket()#声明socket类型，同时生成socket链接对象
client.connect(('localhost',9999))
while True:
    msg=input("通信内容>>：")
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)

    print('recv:',data.decode())

client.close()