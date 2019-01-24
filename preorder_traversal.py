# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return (True if len(self.stack) == 0 else False)
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        return (None if self.isEmpty() else self.stack.pop())

class Solution:
    def Preorder(self, root):
        s = Stack()
        s.push(root)
        
        while not s.isEmpty():
            x = s.pop()
			print(x.val)
            if x.right:
                s.push(x.right)
            if x.left:
                s.push(x.left)
        
