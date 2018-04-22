#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

#浅copy
import copy
person=["name",['a',1000]]

p1=copy.copy(person)
print(p1)
p2=person[:]
p4=person[:]
p3=list(person)
print(p3)

p2[0]='gg'
p4[0]='lala'

p2[1][1]=500

print(p2)
print(p4)


