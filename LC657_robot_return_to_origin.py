class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """        
        sum_ = 0
        dir_val = {'U': 1, 'D': -1, 'L': 2, 'R': -2}
        
        for move in moves:
            sum_ += dir_val[move]
            
        return (True if sum_ == 0 else False)

