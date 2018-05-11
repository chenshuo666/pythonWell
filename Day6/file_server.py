#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import socket,os,hashlib

server=socket.socket()
server.bind(("localhost",6969))
server.listen()

while True:
    conn,address=server.accept()
    print("new conn",conn)
    while True:
        print("Waiting new instruction")
        data=conn.recv(1024)
        if not data:
            print("Client is break")
            break
        cmd,filename= data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f=open(filename,'rb')
            m=hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5 ",m.hexdigest())
            f.close()

            conn.send(m.hexdigest().encode("utf-8"))
        print("Send done")

server.close()