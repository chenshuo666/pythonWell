#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

#装饰器：
#定义：本质是函数，（装饰其他函数）就是为其他函数添加附加功能
#原则：
#1：不能修改被修饰函数的源代码
#2：不能修改被装饰函数的调用方式


'''
实现装饰器知识点
1.函数即是变量
2.高阶函数
    a:把一个函数名当做实参传给另外一个函数
    (在不修改被装饰函数源代码的情况下为其添加功能)
    b:返回值中包含函数名
    c:
3.嵌套函数
'''
import time
# def timmer(func):
#     def warpper(*args,**kwargs):
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print("the func run time is %s "%(stop_time-start_time))
#     return warpper()
#
# @timmer
# def test1():
#     time.sleep(3)
#     print("the time is end ")
#
# test1()

####  修改被修饰函数的调用方式  ####
# def bar():
#     time.sleep(3)
#     print("in the bar ")
#
# def test1(func):
#     print(func)
#     start_time = time.time()
#     func() #运行func地址指向的功能函数
#     stop_time=time.time()
#     print("the func run time is %s "%(stop_time-start_time))
#
# test1(bar)#bar相当于函数的内存地址，找到函数具体功能的门牌号

####  嵌套函数  ####
# def foo():
#     print("in the foo")
#     def bar():
#         print("in the bar")
#
#     bar()
#
# foo()
def timer(func):
    def deco(*arg1,**kwargs):
        start_time=time.time()
        func(*arg1,**kwargs)
        stop_time=time.time()
        print("the time is %s"%(stop_time-start_time))
    return deco

@timer #相当于test1=timer(test1)#获得内存地址的返回值（deco），将返回值变量存到test6中
def test1():
     time.sleep(3)
     print(" in the test1")

@timer #相当于test1=timer(test1)=deco  test2()=deco()
def test2(name):
    time.sleep(3)
    print(" in the test2: "+name)

test1()
test2("lalala")
