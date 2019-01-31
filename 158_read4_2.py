"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Remnants:
    def __init__(self):
        self.remnants = []
        
    def size(self):
        return len(self.remnants)
        
    def push(self, x):
        self.remnants.append(x)
        
    def pop(self):
        if self.size() == 0:
            return None
        data = self.remnants[0]
        del self.remnants[0]
        return data


class Solution:
    def __init__(self):
        self.remnants = Remnants()
        
    def read4n(self, n):
        print('n=', n)
        buf4 = [''] * 4
        count_ = 0
        buf_size = -1
        while count_ <= n and buf_size != 0:
            buf_size = read4(buf4)
            for i in range(0, buf_size):
                self.remnants.push(buf4[i])
                # print('Push ', buf4[i], ', remnants=', self.remnants.remnants)
            
            for _ in range(self.remnants.size()):
                if count_ >= n:
                    break
                i = self.remnants.pop()
                count_ += 1
                yield i
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count_ = 0
        for i in self.read4n(n):
            buf[count_] = i
            count_ += 1
        
        return count_
