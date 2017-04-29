# pylint: disable=redefined-outer-name
class Node:
    def __init__(self, value):
        self.right = self.left = None
        self.data = value

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        """Find the height of tree at given root"""
        #Write your code here
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
