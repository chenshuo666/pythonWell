#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import time

user,password='chenshuo','qwert'
def auth(auth_type):
    print("auth type is ",auth_type)
    def outer_wrapper(func):
        def warpper(*args, **kwargs):
           if auth_type=="local":
               username = input("Please input your name:").strip()
               userpassword = input("please input your password:").strip()

               if user == username and userpassword == password:
                   print("\033[32;1mUser has passed authentication\033[0m")
                   func(*args, **kwargs)
               else:
                   exit("\033[31;1mInvaild username or password\033[0m")
           elif auth_type=="ldap":
               print("dhfgaufhuahg")

        return warpper

    return outer_wrapper

@auth(auth_type='local')
def home ():
    print("welcome to bbs ")

@auth(auth_type='ldap')
def bbs():
    print("welcome to bbs ")

home()