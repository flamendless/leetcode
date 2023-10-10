# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head
        while tail and tail.next:
            temp = tail
            tail = tail.next
            tail.prev = temp
            
            
        l = head
        r = tail
        while l and r:
            if l.val != r.val:
                return False
            
            if not l.next or not r.prev:
                break
            l = l.next
            r = r.prev
            
        return True
        
        
#         values = []
#         length = 0
        
#         cur = head
#         while cur:
#             values.append(cur.val)
#             cur = cur.next
#             length += 1
            
#         l = 0
#         r = length - 1
        
#         while l < r:
#             if values[l] != values[r]:
#                 return False
#             l += 1
#             r -= 1
            
#         return True