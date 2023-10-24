/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int {
    if root == nil {
        return nil
    }
    
    var res []int
    var q []*TreeNode = []*TreeNode{root}
    
    for {
        var level int = len(q)
        if level == 0 {
            break
        }
        
        var min = ^(int(^uint(0) >> 1))
        
        for i := 0; i < level; i++ {
            var node *TreeNode = q[0]
            q = q[1:]
            
            min = int(math.Max(float64(min), float64(node.Val)))
            
            if node.Left != nil {
                q = append(q, node.Left)
            }
            
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        
        res = append(res, min)
    }
    
    
    return res
}