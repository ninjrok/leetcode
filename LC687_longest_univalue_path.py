# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def __init__(self):
        self.count = 0
        
    def lup(self, root):
        if not root:
            return 0
        
        l_count, r_count = 0, 0
        
        l = self.lup(root.left)
        r = self.lup(root.right)
        
        if root.left and root.left.val == root.val:
            l_count = l + 1
        if root.right and root.right.val == root.val:
            r_count = r + 1
            
        self.count = max(self.count, l_count + r_count) 
        
        return max(l_count, r_count)
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lup(root)
        return self.count

