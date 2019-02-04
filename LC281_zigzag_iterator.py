class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1[::-1]
        self.v2 = v2[::-1]
        self.one = True

    def next(self):
        """
        :rtype: int
        """
        if not self.v1 and self.v2:
            return self.v2.pop()
        elif not self.v2 and self.v1:
            return self.v1.pop()
        else:
            if self.one:
                self.one = False
                return self.v1.pop()
            else:
                self.one = True
                return self.v2.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1 or self.v2:
            return True
        
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
