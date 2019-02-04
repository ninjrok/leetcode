class Stack:
    def __init__(self):
        self.array = []
        
    def is_empty(self):
        return (True if len(self.array) == 0 else False)
        
    def push(self, x):
        self.array.append(x)
        
    def pop(self):
        if self.is_empty():
            return None
        
        return self.array.pop()

    
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = Stack()
        open_ = {'(': 1, '{': 2, '[': 3}
        close_ = {')': -1, '}': -2, ']': -3}
        for p in s:
            if p in open_:
                stack.push(p)
            else:
                prev = stack.pop()
                if not prev or open_[prev] + close_[p] != 0:
                    return False
        return (True if stack.is_empty() else False)

