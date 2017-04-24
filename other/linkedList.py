class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        print ('about to run display method')
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new = Node(data)
        current = head
        if current is None:
            current = new
            self.display(head)
            return current
        else:
            while current.next:
                current = current.next
            current.next = new
            self.display(head)
            return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 
