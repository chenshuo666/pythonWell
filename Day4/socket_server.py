#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import socket

server = socket.socket()  # 获得socket实例

server.bind(("localhost", 6969))  # 绑定ip port
server.listen()  # 开始监听

while True:  # 第一层loop
    print("等待客户端的连接...")
    conn, addr = server.accept()  # 接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:", addr)
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break  # 这里断开就会再次回到第一次外层的loop
        print("收到消息:", data)
        conn.send(data.upper())

server.close()
