class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        
        plus_one = []
        carry = 1
        
        while len(digits) > 0:
            digit = digits.pop()
            digit += carry
            d = digit % 10
            carry = digit // 10
            plus_one.append(d)
            
        if carry != 0:
            plus_one.append(carry)
                
        return plus_one[::-1]

