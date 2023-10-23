/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var result *ListNode = &ListNode{}
    var cur *ListNode = result
    
    for {
        if (l1 == nil) && (l2 == nil) {
            break
        }
        
        if l1 != nil {
            cur.Val += l1.Val
            l1 = l1.Next
        }
        
        if l2 != nil {
            cur.Val += l2.Val
            l2 = l2.Next
        }
        
        if cur.Val >= 10 {
            var carry int = cur.Val / 10
            cur.Val = cur.Val % 10
            cur.Next = &ListNode{Val: carry}
        } else if (l1 != nil) || (l2 != nil)  {
            cur.Next = &ListNode{}
        }
        cur = cur.Next
    }
    
    return result
}