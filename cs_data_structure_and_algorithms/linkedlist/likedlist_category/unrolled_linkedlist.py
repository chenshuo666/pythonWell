#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import math
"""
My implementation of an unrolled linked list
Combines the best of arrays and linked lists
Works by having node objects that have arrays in them of a certain max length (16 default)
Append and delete are the basic functions. Dunder methods have been added for all the regular items as well
"""
class UnrolledLinkedList():

    """Node class representing the different lists that make up the unrolled linked list:
    """
    class Node():
        def __init__(self):
            self.items = []
            self.next = None

        def itemsLength(self):
            return len(self.items)

        def hasNext(self):
            return True if self.next != None else False

    """ULL Constructor"""
    def __init__(self, max_node_capacity=16):
        if max_node_capacity <= 0:
            raise ValueError('Node capacity cannot be less than 1')
        self.max_node_capacity = max_node_capacity
        self.head = self.Node()

    """Add the data to the end of the list
     If a node has reached its max capacity, you must create a new node to put the data in"""
    def append(self, data):
        lastNode = self.getLastNode()

        #If there is space in the last node to add the item, do it:
        if lastNode.itemsLength() < self.max_node_capacity:
            lastNode.items.append(data)

        #Otherwise, we need to do some splitting and such before we add it:
        else:
            newNode = self.Node()

            splitIndex = math.ceil(self.max_node_capacity / 2)
            if self.max_node_capacity == 1:
                newNode.items = []
                newNode.items.append(data)
            else:
                newNode.items = lastNode.items[splitIndex:]
                lastNode.items = lastNode.items[: splitIndex]
                newNode.items.append(data)

            lastNode.next = newNode
            lastNode = newNode


    def getLastNode(self):
        thisNode = self.head
        while thisNode.next != None:
            thisNode = thisNode.next
        return thisNode

    """Deletes all the empty nodes (except for the first one - if that's empy then you're in trouble"""
    def removeEmptyNodes(self):
        thisNode = self.head
        checking = True
        while checking:
            if thisNode.next != None and thisNode.next.itemsLength() == 0:
                thisNode.next =  thisNode.next.next
            thisNode = thisNode.next
            if thisNode == None:
                checking = False



    """Remove the item at the given index.
    If the index is negative, then you should remove starting from the back (i.e. deleting at -2 would delete the second-to-last element)
    If the index is too large, raise an IndexError
    """
    def __delitem__(self, index):

        #Reverse it for negative numbers
        if index < 0:
            index = self.__len__() + index

        if self.__len__() <= index:
            raise IndexError("Index range out of bounds")


        count = 0
        thisNode = self.head
        checking = True
        while checking:
            #The index is in this node:
            if count + thisNode.itemsLength() > index and count <= index:
                del thisNode.items[index - count]
                checking = False
                #do some rebalancing:
                self.balance(thisNode)

            count += thisNode.itemsLength()

            #thisNode = thisNode.next
            if thisNode.next != None and thisNode.next.itemsLength == 0:
                thisNode = thisNode.next.next
            else:
                thisNode = thisNode.next
            if thisNode == None:
                checking = False

        self.removeEmptyNodes()

    """Balances this node and everything to the right of it:"""
    def balance(self, node):

        thisNode = node
        while thisNode.itemsLength() <= self.max_node_capacity / 2 and thisNode.hasNext():
            self.__str__()
            thisNode.items.append(thisNode.next.items[0])
            thisNode.next.items = thisNode.next.items[1:]
            self.removeEmptyNodes()
        if thisNode.hasNext() and thisNode.next.itemsLength() < self.max_node_capacity / 2 :
            self.balance(thisNode.next)

    """Returns the item in the given index.
    If the index is negative, return with the index starting from the back (i.e. getting at -1 returns the last item)
    If the index is too large, raise an IndexError
    """
    def __getitem__(self, index):
        thisNode = self.head

        #Reverse it for negative numbers
        if index < 0:
            index = self.__len__() + index
        if index >= self.__len__() or index < 0:
            raise IndexError

        count = 0
        checking = True
        while checking:
            #The index is in this node:
            if count + thisNode.itemsLength() > index and count <= index:
                checking = False
                return thisNode.items[index - count]
            count += thisNode.itemsLength()
            thisNode = thisNode.next


    """sets the item at key to value
    If the key is too large, raise an IndexError
    """
    def __setitem__(self, key, value):

        #Reverse it for negative numbers
        if key < 0:
            key = self.__len__() + key

        if key >= self.__len__():
            raise IndexError

        thisNode = self.head
        self.__str__()
        print(key)
        print(value)
        count = 0
        checking = True
        while checking:
            #The index is in this node:
            if count + thisNode.itemsLength() > key and count <= key:
                checking = False
                thisNode.items[key - count] = value

            count += thisNode.itemsLength()
            if thisNode.next != None:
                thisNode = thisNode.next




    """Use the Python yield statement to make your list iterable. This will allow you to use it in a for-each loop
    """
    def __iter__(self):
        thisNode = self.head

        while thisNode != None:
            for item in thisNode.items:
                yield item
            thisNode = thisNode.next


    """reverse of iter
    """
    def __reversed__(self):
        #Reverse the list
        thisNode = self.head
        thisList = []

        while thisNode != None:
            for item in thisNode.items:
                thisList.append(item)
            thisNode = thisNode.next
        for i in thisList[::-1]:
            yield i



    """Create a string representation of the list in the form {[x, x, x], [x, x], [x, x, x, x]} where each set of [] indicates the list of values within a single node.
        returns the string as well for testing purposes
    """
    def __str__(self):
        thisNode = self.head
        toPrint = "{"
        if thisNode.itemsLength() != 0:
            toPrint += str(thisNode.items)


        while thisNode.next != None:
            thisNode = thisNode.next
            toPrint += ", " + str(thisNode.items)

        toPrint += "}"
        print(toPrint)
        return toPrint

    """returns the total # of data in the list, not the number of nodes
    """
    def __len__(self):

        counting = True
        count = 0
        thisNode = self.head
        while counting:
            if thisNode.itemsLength() == 0:
                counting = False
            else:
                count += thisNode.itemsLength()
                if not thisNode.hasNext():
                    counting = False
                else:
                    thisNode = thisNode.next
        return count



    """Returns True if obj is in the data structure, otherwise False
    """
    def __contains__(self, obj):
        thisNode = self.head

        while thisNode != None:
            for val in thisNode.items:
                if obj == val:
                    return True

            thisNode = thisNode.next

        return False
