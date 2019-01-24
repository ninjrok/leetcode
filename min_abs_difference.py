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
        if len(self.stack) == 0:
            return None
        
        value = self.stack[-1]
        del self.stack[-1]
        return value

class Solution:
    def getMinimumDifference(self, root):
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
            
        diffs = []
        for idx, val in enumerate(inorder):
            diffs.append(abs(inorder[idx-1] - inorder[idx]))
                         
        return min(diffs) 
