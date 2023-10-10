# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def rec(cur_depth, node):
            if not node:
                return 0
            
            cur_depth += 1
            l = rec(cur_depth, node.left)
            r = rec(cur_depth, node.right)
            return max(cur_depth, max(l, r))
        
        return rec(0, root)