#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import paramiko

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='c1.salt.com',port=22,username='wupeiqi',password='123')

stdin,stdout,stderr=ssh.exec_command('df')

result=stdout.read()

ssh.close()