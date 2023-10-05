# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) and (not list2):
            return list1


        a = []
        ah = list1
        bh = list2
        
        while ah:
            a.append(ah.val)
            ah = ah.next
            
        while bh:
            a.append(bh.val)
            bh = bh.next
        
        a.sort()
        
        head = ListNode()
        cur = head
        
        for i in range(len(a)):

            cur.val = a[i]
            
            if i == len(a) - 1:
                break

            cur.next = ListNode()
            cur = cur.next
            
            
        return head
  
