import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    queue = []

    def enqueue(self, node):
        self.queue.insert(0, node)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def levelOrder(self, root):
        if root is not None:
            self.enqueue(root)
            while self.queue:
                tree = self.dequeue()
                print(tree.data)
                if tree.left is not None:
                    self.enqueue(root.left)
                if tree.right is not None:
                    self.enqueue(root.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

