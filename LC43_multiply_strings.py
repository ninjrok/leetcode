class Solution:
    def str_to_int(self, num):
        num_int = None
        if num == '0':
            num_int = 0
        elif num == '1':
            num_int = 1
        elif num == '2':
            num_int = 2
        elif num == '3':
            num_int = 3
        elif num == '4':
            num_int = 4
        elif num == '5':
            num_int = 5
        elif num == '6':
            num_int = 6
        elif num == '7':
            num_int = 7
        elif num == '8':
            num_int = 8
        elif num == '9':
            num_int = 9
        return num_int
            
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        inter = []
        if len(num1) > len(num2):
            temp = num1
            num1 = num2
            num2 = temp
        inter_loop = 0
        for i in reversed(num1):
            carry, place, inter_sum = 0, 0, 0
            for j in reversed(num2):
                val = self.str_to_int(j) * self.str_to_int(i)
                inter_sum += pow(10, place) * ((val % 10) + carry)
                carry = val // 10
                place += 1
            inter.append((carry * pow(10, place) + inter_sum) * pow(10, inter_loop))
            inter_loop += 1
            
        return str(sum(inter))

