import random

class Codec:
    def __init__(self):
        self.encodings = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        rand_hash = random.randint(1, 101)
        enc = 0
        
        for char in longUrl:
            enc += rand_hash * 31 + ord(char)
            
        self.encodings[enc] = longUrl
        
        return enc
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.encodings[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

