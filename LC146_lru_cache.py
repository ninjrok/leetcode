class Queue:
    def __init__(self):
        self.array = []
        
    def enqueue_back(self, data):
        self.array.append(data)
        
    def dequeue_front(self):
        if len(self.array) == 0:
            return None
        data = self.array[0]
        del self.array[0]
        
        return data

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.queue = Queue()
        
        
    def update_lru(self, key):
        try:
            idx = self.queue.array.index(key)
            self.queue.enqueue_back(key)
            del self.queue.array[idx]
        except:
            self.queue.enqueue_back(key)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.update_lru(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache and len(self.cache) == self.capacity:
            key_idx = self.queue.dequeue_front()
            del self.cache[key_idx]

        self.cache[key] = value
        self.update_lru(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
