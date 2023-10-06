class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        d, m = divmod(n, 3)
        
        if m == 0:
            return 3 ** d
        
        if m == 1:
            return 3 ** (d - 1) * 4
        
        return 3 ** d * 2