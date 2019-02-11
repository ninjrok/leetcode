class Solution:
    def __init__(self):
        self.symbols = {1: 'I', 5: 'V', 10: 'X', 
                        50:'L', 100: 'C', 500: 'D', 
                        1000: 'M'}
        
    def num_generator(self, num):
        c = 0
        while num > 0:
            c += 1
            i = num % 10
            num //= 10
            yield c, i
        
    def place_value(self, value, base, mid, high):
        if value == 4:
            return self.symbols[mid] + self.symbols[base]
        elif value == 9:
            return self.symbols[high] + self.symbols[base]
        elif value < 4:
            return self.symbols[base] * value
        else:
            return (value - 5) * self.symbols[base] + self.symbols[mid]
            
    def roman_numeral(self, place, value):
        if place == 1:
            # Units Place
            return self.place_value(value, 1, 5, 10)
        elif place == 2:
            # Tens Place
            return self.place_value(value, 10, 50, 100)
        elif place == 3:
            # Hundredths Place
            return self.place_value(value, 100, 500, 1000)
        elif place == 4:
            # Thousands Place
            return self.symbols[1000] * value
                
        return roman_str

    def intToRoman(self, num: 'int') -> 'str':
        roman = ""
        
        for idx, val in self.num_generator(num):
            roman += self.roman_numeral(idx, val)
        
        return roman[::-1]

