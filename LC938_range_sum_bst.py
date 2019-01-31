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
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = Stack()
        idx = 0
        inorder_list = []
        
        while 1:
            while root:
                s.push(root)
                root = root.left
                
            if s.isEmpty():
                break
                
            root = s.pop()
            if root.val == L:
                l_idx = idx
            if root.val == R:
                r_idx = idx
            idx += 1
            inorder_list.append(root.val)
            root = root.right

        return sum(inorder_list[l_idx:r_idx+1])
