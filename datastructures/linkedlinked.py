#!/usr/bin/python3

class LinkedList:
    def __init__(self, d):
        self.head = Node(d)
    def printList(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
    def appendToTail(self, d):
        new = Node(d)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new
    def remove(self, d):
        #search through list, return true if delete succeeds
        cur = self.head
        status = False
        if cur.data == d:
            self.head = cur.next
        else:
            while cur.next != None:
                prev = cur
                cur = cur.next
                if cur.data == d:
                    prev.next = cur
                    status = True
                    break
        #if not exist return - false
        return status

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
