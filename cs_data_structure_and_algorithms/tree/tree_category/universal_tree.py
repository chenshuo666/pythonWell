#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
# import queue
# import treelib
#
# class Node:
#     def __init__(self,data,first_child=None,next_sibling=None):
#         self.data = data
#         self.first_child = first_child
#         self.next_sibling = next_sibling
#
# class UniversalTree(object):
#     def __init__(self,n):
#         self.root = None
#         self.node_number = 0
#         self.fork = n
#
#     def add(self, data):
#         """create complete n tree"""
#         global pop_node
#         count_inner =0
#         count_outside = 0
#         node = Node(data)
#         q = queue.LifoQueue()
#
#         if self.root is None:
#             self.root = node
#             q.put(self.root)
#
#         else:
#             if count_outside == 0:
#                 pop_node = q.get()
#
#             if count_inner < self.fork:
#                 if pop_node.next_sibling ==None:
#                     pop_node.next_sibling = node
#                     q.put(pop_node.next_sibling)
#                     count_inner += 1
#                     return
#                 else:
#                     pop_node = pop_node.next_sibling
#                     pop_node.next_sibling = node
#                     q.put(pop_node.next_sibling)
#                     count_inner += 1
#                     return
#
#             elif pop_node.first_child is None:
#                 pop_node.first_child = node
#                 q.put(pop_node.first_child)
#                 return

class node:
    def __init__(self, data):
        self._data = data
        self._children = []

    def getdata(self):
        return self._data

    def getchildren(self):
        return self._children

    def add(self, node):
        ##if full
        if len(self._children) == 4:
            return False
        else:
            self._children.append(node)

    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None


class tree:
    def __init__(self):
        self._head = node('header')

    def linktohead(self, node):
        self._head.add(node)

    def insert(self, path, data):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return False
            else:
                cur = cur.go(step)
        cur.add(node(data))
        return True

    def search(self, path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return None
            else:
                cur = cur.go(step)
        return cur

if __name__=="__main__":

    '''
    define node
    '''
    a = node('A')
    b = node('B')
    c = node('C')
    d = node('D')
    e = node('E')
    f = node('F')
    g = node('G')
    h = node('H')
    i = node('I')
    j = node('J')
    k = node('K')
    l = node('L')
    m = node('M')
    n = node('N')
    o = node('O')

    '''
    adding node to build true
    '''
    a.add(b)
    a.add(g)
    a.add(h)
    b.add(c)
    b.add(e)
    g.add(i)
    g.add(j)
    g.add(k)
    g.add(l)
    h.add(m)
    h.add(n)
    h.add(o)
    c.add(d)
    c.add(f)
    i.add(node(29))
    j.add(node(28))
    k.add(node(27))
    l.add(node(26))
    m.add(node(25))
    n.add(node(24))
    o.add(node(23))
    f.add(node(30))

    tree = tree()
    tree.linktohead(a)

    # testcase
    print('Node', tree.search("ABE").getdata())
    print('Node', tree.search("ABC").getdata())
    print('Node', tree.search("AHM").getdata())
    tree.insert("ABCD", 1)
    for i in d.getchildren():
        print('value after', d.getdata(), ' is ', i.getdata())