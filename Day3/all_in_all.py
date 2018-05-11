#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

"""

类
    属性
        实例变量
        类变量
        私有属性__var
    方法
       构造方法，
       析构函数
       私有方法

对象:实例化一个类之后得到的对象

封装
   把一些功能的实现细节不对外暴露

继承
    继承 ，组合
    代码的重用
    单继承
    多继承，
        2.7 经典类，深度优先，  新式类，广度优先
        3.x 均是广度优先
        class Foo(object):
            def __init__(self,name,age,sex,salary,course):

                self.salary = salary
                self.course = course



多态
    接口重用， 一种接口，多种实现

静态方法
    只是名义上归类管理， 实际上在静态方法里访问不了类或实例中的任何属性
类方法
    只能访问类变量，不能访问实例变量

属性方法
    把一个方法变成一个静态属性

反射
    hasattr(obj,name_str) , 判断一个对象obj里是否有对应的name_str字符串的方法
    getattr(obj,name_str), 根据字符串去获取obj对象里的对应的方法的内存地址
    setattr(obj,'y',z), is equivalent to ``x.y = v''
    delattr
异常
    try :
        code
    except (Error1,Erro2) as e:
        print e

    except Exception :抓住所有错误，不建议用

Socket网络编程

"""
class person(object):
    """描述人的类"""

    def __init__(self,name,age,height,weight,address):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.address=address

    def eat(self,food):
        print("{} is eating {}".format(self.name,food))

def buff(self):
    print('{} have a baby'.format(self.name))

p1=person('chenshuo',21,188,75,'nuaa')
print(p1.__doc__)
choice= input('>>:')

if hasattr(p1,choice):
    func=getattr(p1,choice)
    func('baozi')
else:
    """
    p1.choice=buff,在p1对象中创建buff函数，buff函数的名称变为choice，功能保持一致
    将choice的名称变为func相当于 def func(p1)
       
    """
    setattr(p1,choice,buff)
    func1=getattr(p1,choice)
    print(func1)
    func1(p1)


