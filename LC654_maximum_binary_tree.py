class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        max_ = 0
        for i in range(len(nums)):
            if nums[max_] < nums[i]:
                max_ = i
        
        root = TreeNode(x=nums[max_])
        root.left = self.constructMaximumBinaryTree(nums[:max_])
        root.right = self.constructMaximumBinaryTree(nums[max_+1:])
        
        return root

