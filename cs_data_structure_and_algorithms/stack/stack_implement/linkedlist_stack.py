#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node(object):
    def __init__(self,data): #定位的点的值和一个指向
        self.data=data    #指向元素的值,原队列第二元素
        self.next=None   #指向的指针

class LinkedListStack(object):
    def __init__(self,max_capacity):
        self.top=None #初始化最开始的位置
        self.max_capacity = max_capacity
        self.length = 0

    def get_top(self):  #获取栈顶的元素
        if self.top!=None:  #如果栈顶不为空
            return self.top.data  #返回栈顶元素的值
        else:
            return None

    def size(self):
        """获取栈的大小"""
        return self.length
        # current_node = self.top
        # if current_node:
        #     i = 1
        #     while current_node.next:
        #         current_node = current_node.next
        #         i += 1
        #     return i
        # else:
        #     return 0

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def isStackFull(self):
        if self.size()==self.max_capacity:
            return True
        else:
            return False

    def push(self,node_instantiation):#添加到栈中
        if self.isStackFull() :
            print("the stack is full")
        else:
            node_instantiation=Node(node_instantiation)  #实例化节点
            node_instantiation.next=self.top  #顶端元素传值给一个指针
            self.top=node_instantiation
            self.length += 1
            return node_instantiation.data


    @property
    def pop(self):  #出栈
        if self.top == None:
            return None
        else:
            tmp=self.top.data
            self.top=self.top.next  #下移一位，进行
            self.length -= 1
            return tmp

    def travel_print(self):
        """
        遍历整个栈，并输出栈的值
        """
        if self.isEmpty():
            print("Stack's length is 0")
        else:
            node = self.top
            print("top -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def clear_linkedlist_stack(self):
        self.top = None
        self.length = 0
        print("the stack is empty")




if __name__=="__main__":
    s=LinkedListStack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.travel_print()
    print(s.get_top())
    print(s.isStackFull())
    print(s.size())
    print("############")
    print(s.pop)
    print(s.pop)
    print(s.pop)

    s.push(11)
    s.push(22)
    s.push(32)
    s.travel_print()
    s.clear_linkedlist_stack()
    s.travel_print()