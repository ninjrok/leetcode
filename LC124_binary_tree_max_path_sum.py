# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_path_sum = float('-inf')
        
    def max_gain(self, root):
        if not root:
            return 0
        
        l = max(self.max_gain(root.left), 0)
        r = max(self.max_gain(root.right), 0)
        
        self.max_path_sum = max(self.max_path_sum, root.val + l + r)
        
        return root.val + max(l, r)
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_gain(root)
        return self.max_path_sum

