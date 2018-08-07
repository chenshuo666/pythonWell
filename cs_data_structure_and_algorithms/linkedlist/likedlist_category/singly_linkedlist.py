#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

"""Initialize the node, the node includes the currently stored content and a pointer to the next node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        SinglyLinkedList 的初始化
        """
        self.length = 0
        self._head = None

    def is_empty(self):
        """
        判断该链表是否为空
        """
        if self._head == None:
            return True
        else:
            return False

    def get_length(self):
        """
        获取链表长度
        """
        current_node = self._head
        if current_node:
            i = 1
            while current_node.next:
                current_node = current_node.next
                i += 1
            return i
        else:
            return 0

    def get_data_by_index(self, index):
        j = 0
        p = self._head
        if self.is_empty():
            print('Linklist is empty.')
            return

        else:

            while p.next != 0 and j < index:
                p = p.next
                j += 1
            if j == index:
                return p.data
            else:
                print('Target is not exist!')

    def get_data_by_self(self, data):
        """查找元素是否存在"""
        cur = self._head
        j = 0
        if self.is_empty():
            print('Linklist is empty.')
            return

        else:
            while cur != None:
                if cur.data == data:
                    print("the index of the %s is %s".format(data, j))
                    return True
                cur = cur.next
                j += 1
            return False


    def travel_print(self):
        """
        遍历整个链表，并输出链表的值
        """
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self._head
            print("_head -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def append(self, this_node):
        """
        在链表末添加node/值,如果是node对象直接添加，否则先转换为node对象
        :param this_node: 数据或者node对象
        :return: None
        """
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            # 链表为空的情况将头指针指向当前node
            self._head = this_node
        else:
            node = self._head
            while node.next:
                node = node.next
            node.next = this_node
        self.length += 1

    def insert(self, value, index):
        """
        链表的插入操作
        :param value: 要插入的值
        :param index: 位置
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index value is out of range.")
                return
            else:
                # 获得当前node对象和_head
                this_node = Node(data=value)
                current_node = self._head

                if index == 0:
                    # 索引值为0是将
                    self._head = this_node
                    this_node.next = current_node
                    return

                while index - 1:
                    current_node = current_node.next
                    index -= 1

                # 这两条语句顺序很关键
                # 将当前节点与后一个节点拆开，this_node指向后一个节点，前一个节点指向this_node
                this_node.next = current_node.next
                current_node.next = this_node
                self.length += 1
                return

        else:
            print("Index value is not int.")
            return


    def delete_node(self, index):
        """
        删除链表中某个位置的节点
        :param index: 位置索引
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    self._head = self._head.next
                else:
                    current_node = self._head
                    while index - 1:
                        current_node = current_node.next
                        index -= 1
                    current_node.next = current_node.next.next
                    self.length -= 1
                    return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """为链表中某个位置的节点修改值"""

        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.next = self._head.next
                    self._head = this_node
                else:
                    current_node = self._head
                    while index - 1:
                        current_node = current_node.next
                        index -= 1
                    this_node.next = current_node.next.next
                    current_node.next = this_node
                    return
        else:
            print("Index value is not int.")
            return

    def get_value(self, index):
        """
        获取链表中某个位置节点的值
        :param index: 位置索引
        :return: 该节点值, int or not
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    return self._head.data
                else:
                    current_node = self._head
                    while index - 1:
                        current_node = current_node.next
                        index -= 1
                    return current_node.next.data
        else:
            print("Index value is not int.")
            return

    def clear_singly_linkedlist(self):
        """
        清空链表

        """
        self._head = None
        self.length = 0
        print("Clear the linked list finished.")





if __name__ == '__main__':
    node1 = Node(data='node1')
    node2 = Node(data='node2')
    linked_list = SinglyLinkedList()
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.travel_print()
    linked_list.insert("sdf", 1)
    linked_list.travel_print()
    # linked_list.delete_node(0)
    linked_list.update(value="update_test", index=2)
    linked_list.travel_print()
    print(linked_list.get_value(index=2))
    print(linked_list.get_length())
    print(linked_list.is_empty())