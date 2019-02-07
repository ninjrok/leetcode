class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if not haystack and not needle:
            return 0
        
        l = len(needle)
        found = False
        for i in range(len(haystack)):
            if needle == haystack[i:i+l]:
                found = True
                break
                
        return (i if found else -1)

