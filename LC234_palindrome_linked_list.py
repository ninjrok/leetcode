# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow_ptr = fast_ptr = head
        
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
                
        stack = []
            
        while slow_ptr:
            stack.append(slow_ptr.val)
            slow_ptr = slow_ptr.next
            
        while head and stack:
            if head.val != stack.pop():
                return False
            head = head.next
            
        return True

