class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        
        
    def size(self):
        return len(self.array)


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.array.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        return (None if self.size() == 0 else self.array.pop())

    
    def top(self):
        """
        :rtype: int
        """
        return (None if self.size() == 0 else self.array[-1])
        

    def getMin(self):
        """
        :rtype: int
        """
        return (None if self.size() == 0 else min(self.array))
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

