class Stack:
    def __init__(self):
        self.arr = []
        
    def is_empty(self):
        return (True if not self.arr else False)
    
    def top(self):
        return (self.arr[-1] if not self.is_empty() else None)
    
    def push(self, x):
        self.arr.append(x)
        
    def pop(self):
        return (self.arr.pop() if not self.is_empty() else None)


class Solution:
    def __init__(self):
        self.stack = Stack()
        self.stack.push(-1)
        self.max = 0
    
    def longestValidParentheses(self, s: 'str') -> 'int':
        for i in range(len(s)):
            if s[i] == '(':
                self.stack.push(i)
            else:
                self.stack.pop()
                if self.stack.is_empty():
                    self.stack.push(i)
                else:
                    self.max = max(self.max, i - self.stack.top())
                
        return self.max

