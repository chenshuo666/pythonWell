#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import getpass

count=0
name='chenshuo'
password='qwert12345'
print("You have only 3 chances!!!")

for i in range(3):

    _name = input("name:")
    _password = getpass.getpass("password:")
    if _name==name and _password ==password:
        print("welcome {} to the website".format(_name))
        print(_name,_password)
        break
    else:
        print("Invalid username and password! please try again..")
        count+=1
if count==3:
    print("Your account is Locked !")