# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_length = 0
    
    def longest(self, root):
        if not root:
            return 0
        
        l = self.longest(root.left) + 1
        r = self.longest(root.right) + 1
        
        if root.left and root.left.val - root.val != 1:
            l = 1
        if root.right and root.right.val - root.val != 1:
            r = 1
        
        length = max(l, r)
        self.max_length = max(length, self.max_length)
        
        return length

    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest(root)
        
        return self.max_length

