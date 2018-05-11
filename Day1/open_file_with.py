#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import sys
with open ('ali.txt','r',encoding='utf-8') as f:#对文件操作完成后自动关闭文件
    #可同时打开多个文件
    for line in f.readlines():
        print(line.strip())
def null_1():
    print('return:')#return可以返回多个值，返回的值存在一个元组中
x=null_1()
print(x)
def func(x,y,z):
    print(x)
    print(y)
    print(z)

func(3,6,z=5)#位置参数只能放在关键字参数之前
#实参与形参一一对应；关键字调用；位置不需要固定
func(3,z=3,y=9)

print("----------------------------------")

#默认参数特点：调用函数的时候，默认参数非必须传递
def func_2(x,y=2):
    print(x)
    print(y)

func_2(1)

print("------------------------------------")

#参数组类型
def test(x,*args):
    print(x)
    print(args)

test(1,2,3,4,5,76,4)

#**kwargs:把N个关键字参数，转化成字典的形式
def test_1(**kwargs):
    print(kwargs)
    print(kwargs['name'])

test_1(name='chenshuo',age=18,sex='Boy')
test_1(**{'name':'chenshuo','age':15,'sex':'boy'})

print('---------------------------------------')

#全局变量最好不要定义在函数中
#列表和字典的数据可以通过修改局部变量来修改全局变量
def change_name():
    global name
    name="name"

change_name()
print(name)


def calc(n):
    print(n)
    return calc(n+1)

calc(0)



