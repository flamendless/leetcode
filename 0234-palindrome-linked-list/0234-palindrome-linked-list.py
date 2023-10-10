# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        length = 0
        
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
            length += 1
            
        l = 0
        r = length - 1
        
        while l < r:
            if values[l] != values[r]:
                return False
            l += 1
            r -= 1
            
        return True