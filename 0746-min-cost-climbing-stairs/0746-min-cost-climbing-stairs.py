class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c = {}
        
        def rec(i):
            if i <= 1:
                return 0
            if i in c:
                return c[i]
            
            one = cost[i - 1] + rec(i - 1)
            two = cost[i - 2] + rec(i - 2)
            c[i] = min(one, two)
            return c[i]
        
        return rec(len(cost))