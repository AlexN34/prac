#!/usr/bin/python3

class MyDoubleLinkedList(self):
    head = None
    tail = None

    def insertAtEnd(self, node):
        new = Node()
        if len(self) == 0:
            self.head = new
            self.tail = new

        else:
            new.prev = tail
            self.tail.next = new
    def remove(self, node):
        cur = self.head
        while cur != None:
            if cur.data == node.data:
                prev.next = cur.next
                cur.next.prev = prev
                break
            prev = cur
            cur = cur.next



class Node(self):
    data = None
    next = None
    prev = None
