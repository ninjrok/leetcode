class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        return nums
        
    
    def wiggleSort(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if (i%2==0 and nums[i]>nums[i+1]) or (i%2==1 and nums[i+1]>nums[i]):
                nums = self.swap(nums, i, i+1)

