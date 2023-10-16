class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        s = set()
        
        while True:
            
            total = 0
            while n:
                n, d = divmod(n, 10)
                total += d ** 2
                
            if total in s:
                return False
                
            s.add(total)
            n = total
            if n == 1:
                return True
            
        return False
                
            