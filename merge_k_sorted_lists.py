# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Heap:
    def __init__(self):
        self.array = []
        
    def percolate_down(self, i):
        l = (2*i+1 if (2*i+1) < len(self.array) else None)
        r = (2*i+2 if (2*i+2) < len(self.array) else None)
        
        if l and self.array[l] < self.array[i]:
            minimum = l
        else:
            minimum = i
        if r and self.array[r] < self.array[minimum]:
            minimum = r
            
        if minimum != i:
            temp = self.array[i]
            self.array[i] = self.array[minimum]
            self.array[minimum] = temp
            self.percolate_down(minimum)
            
    def delete_min(self):
        if len(self.array) == 0:
            return None
        
        data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.percolate_down(0)
        
        return data
            
    def build_heap(self, linked_lists):
        for head in linked_lists:
            while head:
                self.array.append(head.val)
                head = head.next
                
        i = (len(self.array)-1)//2
        while i >= 0:
            self.percolate_down(i)
            i -= 1

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k_sorted_list = []
        h = Heap()
        h.build_heap(lists)
        
        for _ in range(0, len(h.array)):
            k_sorted_list.append(h.delete_min())
        
        return k_sorted_list

