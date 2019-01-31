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
        return (None if len(self.stack) == 0 else self.stack.pop())

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = Stack()
        inorder = []
        
        while 1:
            while root:
                s.push(root)
                root = root.left
                
            if s.isEmpty():
                break
                
            root = s.pop()
            inorder.append(root.val)
            root = root.right
            
        return min([abs(inorder[i] - inorder[i-1]) for i in range(len(inorder))])
