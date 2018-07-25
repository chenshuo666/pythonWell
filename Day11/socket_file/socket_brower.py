#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import socket

def link_socket(client):
    buf= client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    f=open('login_blog.html','rb')
    data=f.read()
    f.close()
    client.send(data)

def main():
    socket_object=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_object.bind(('localhost',8000))
    socket_object.listen(5)

    while True:
        conn,address= socket_object.accept()
        link_socket(conn)
        conn.close()


if __name__=='__main__':
    main()