class Solution:
    def index_of(self, longest, char):
        try:
            return longest.index(char)
        except:
            return False
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        longest = ''
        substring_len = 0
        
        for i in range(0, len(s)):
            idx = self.index_of(longest, s[i])
            if type(idx) == int:
                if substring_len < len(longest):
                    substring_len = len(longest)
                if longest[idx] == s[i-1]:
                    longest = s[i]
                else:
                    longest = longest[idx+1:] + s[i]
            else:
                longest += s[i]
                if substring_len < len(longest):
                    substring_len = len(longest)
        
        return substring_len

