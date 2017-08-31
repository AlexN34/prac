class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        #Write your code here
        if head.data == None:
            return
        prev = head
        cur = head
        stack = [cur.data]
        counter = 0
        while cur.next != None:
            if prev is not None and cur is not None:
                print("items are: {}, {}, next is: {}".format(
                    prev.data, cur.data, cur.next))
            cur = cur.next
            if cur.data not in stack:
                stack.append(cur.data)
                prev = cur
            else:
                prev.next = cur.next
                print("redirect!")
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
