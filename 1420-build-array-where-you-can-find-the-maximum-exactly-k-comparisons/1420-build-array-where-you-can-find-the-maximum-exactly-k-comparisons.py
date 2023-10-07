class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = (10 ** 9) + 7
        
        dp = {}
        
        def rec(i, cur, cost, r):
            key = (i, cur, cost)
            if key in dp:
                return dp[key]
            
            if (i == 1) and (cost == 1):
                return 1
            
            if (i == 1) or (cost == 0):
                return 0
            
            n = 0
            for j in range(1, r + 1):
                if j <= cur:
                    n += rec(i - 1, cur, cost, r)
                else:
                    n += rec(i - 1, j, cost - 1, r)
                    
            dp[key] = n % mod
            return dp[key]
        
        res = 0
        for i in range(1, m + 1):
            res = (res + rec(n, i, k, m)) % mod
            
        return res
                