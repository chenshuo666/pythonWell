
#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import socket,hashlib
client = socket.socket()

client.connect(('localhost',6969))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode("utf-8"))
        server_response = client.recv(1024)  ##接受命令结果的长度
        print("server response:",server_response)
        client.send("准备好接受数据".encode("utf-8"))
        received_size = 0
        filename1 =cmd.split()[1]
        f=open(filename1 + ".new",'wb')
        file_size= int(server_response.decode())
        m=hashlib.md5()
        while received_size < file_size:
            if file_size - received_size>1024:
                size= 1024
            else:
                size= file_size-received_size
            data = client.recv(size)
            received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
            # print(data.decode())
            m.update(data)
            f.write(data)
        else:
            new_file_md5= m.hexdigest()

            print("cmd res receive done...", received_size)
            f.close()


        server_file_md5=client.recv(1024)
        print(new_file_md5)
        print(server_file_md5)



client.close()