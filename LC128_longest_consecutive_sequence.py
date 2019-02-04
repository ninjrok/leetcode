class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_consec_seq = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_longest_seq = 1
                curr_num = num
                
                while curr_num + 1 in nums_set:
                    curr_longest_seq += 1
                    curr_num += 1
                    
                longest_consec_seq = max(curr_longest_seq, longest_consec_seq)

        return longest_consec_seq

