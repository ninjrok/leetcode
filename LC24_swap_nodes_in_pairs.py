# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Stack:
    def __init__(self):
        self.arr =[]
        
    def size(self):
        return len(self.arr)
        
    def is_empty(self):
        return (True if self.size() == 0 else False)
    
    def push(self, x):
        self.arr.append(x)
        
    def pop(self):
        return (None if self.is_empty() else self.arr.pop())


class Solution:
    def __init__(self):
        self.stack = Stack()
        
    def swap(self, node1, node2):
        if not node1 or not node2:
            return node1
        
        temp = node2.next
        node2.next = node1
        node1.next = temp
        
    
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        elif not head.next:
            return head
            
        while head:
            self.stack.push(head)
            head = head.next
        
        while self.stack.size() >= 2:
            if self.stack.size() % 2 != 0:
                self.stack.pop()
                continue
            node2 = self.stack.pop()
            node1 = self.stack.pop()
            self.swap(node1, node2)
            top = self.stack.pop()
            if top:
                top.next = node2
                self.stack.push(top)
                
        return node2

