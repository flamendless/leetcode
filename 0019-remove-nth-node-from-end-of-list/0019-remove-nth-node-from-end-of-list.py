# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        
        for _ in range(n):
            l = l.next
            
        if not l:
            return head.next
        
        while l.next:
            l, r = l.next, r.next
        r.next = r.next.next
        return head