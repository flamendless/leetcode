# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        slow = head
        fast = head.next
        
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                fast = fast.next
            else:
                slow.next = fast.next
                fast = slow.next
            
        return head
                