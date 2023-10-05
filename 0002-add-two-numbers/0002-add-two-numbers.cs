/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node = l1;
        ListNode node2 = l2;
        
        ListNode sol = new ListNode(0, null);
        ListNode head = sol;
        
        while (true)
        {
            int a = (node != null) ? node.val : 0;
            int b = (node2 != null) ? node2.val : 0;
            int sum = a + b + sol.val;                  
            sol.val = sum % 10;
            int carry = sum / 10;   
            
            if ((node != null && node.next != null) ||
                (node2 != null && node2.next != null) ||
                carry != 0)
            {
                node = node != null ? node.next : null;
                node2 = node2 != null ? node2.next : null;  
                sol.next = new ListNode(carry, null);
                sol = sol.next; 
            }
            else
                break;
        }
        
        return head;
    }
}