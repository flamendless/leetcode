# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def rec(node, cur):
            if not node:
                return False
            
            cur += node.val
            if (
                (cur == targetSum) and
                (not node.left) and
                (not node.right)
            ):
                return True
            
            
            
            l = rec(node.left, cur)
            r = rec(node.right, cur)
            return l or r
        
        return rec(root, 0)