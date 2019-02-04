# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    def __init__(self):
        self.array = []
        
    def is_empty(self):
        return (True if len(self.array) == 0 else False)
        
    def enqueue(self, x):
        self.array.append(x)
        
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.array[0]
        del self.array[0]
        
        return data

class Heap:
    def __init__(self):
        self.array = []
    
    def is_empty(self):
        return (True if len(self.array) == 0 else False)
        
    def percolate_down(self, i):
        l = (2*i+1 if (2*i+1) < len(self.array) else None)
        r = (2*i+2 if (2*i+2) < len(self.array) else None)
        
        if l and self.array[l] < self.array[i]:
            min_ = l
        else:
            min_ = i
        if r and self.array[r] < self.array[min_]:
            min_ = r
            
        if min_ != i:
            temp = self.array[min_]
            self.array[min_] = self.array[i]
            self.array[i] = temp
            self.percolate_down(min_)
            
    def delete_min(self):
        if self.is_empty():
            return None
        
        data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.percolate_down(0)
        
        return data
            
    def levelorder(self, root):
        if not root:
            return False
        
        queue = Queue()
        queue.enqueue(root)
        
        while not queue.is_empty():
            data = queue.dequeue()
            self.array.append(data.val)
            if data.left:
                queue.enqueue(data.left)
            if data.right:
                queue.enqueue(data.right)
                
        return True
            
    def build_heap(self, root):
        # Traverse tree level order
        if self.levelorder(root):
            i = (len(self.array) - 1) // 2

            while i >= 0:
                self.percolate_down(i)
                i -= 1

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.min_heap = Heap()
        self.min_heap.build_heap(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        # print(self.min_heap.array)
        return self.min_heap.delete_min()
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        # print(self.min_heap.array)
        return not self.min_heap.is_empty()
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

