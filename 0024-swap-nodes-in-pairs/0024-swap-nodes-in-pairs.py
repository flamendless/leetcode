# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        left = None
        right = head
        final = head.next
        
        while right and right.next:
            temp = right.next
            if left:
                left.next = temp
                
            right.next, temp.next = temp.next, right
            left, right = right, right.next
        
        return final or head
            
            