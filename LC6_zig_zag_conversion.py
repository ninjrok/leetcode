class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        zigzag = [ [None] for i in range(numRows) ]
        row_order = [i for i in range(0, numRows)]
        row_order  = row_order + list(reversed(row_order[:-1]))
        row_count = 0
        
        for i in range(len(s)):
            if row_count > len(row_order) - 1:
                row_count = 1
            zigzag[row_order[row_count]].append(s[i])
            row_count += 1
        
        zig_zag = ''
        for list_ in zigzag:
            del list_[0]
            zig_zag += ''.join(list_)
        
        return zig_zag

