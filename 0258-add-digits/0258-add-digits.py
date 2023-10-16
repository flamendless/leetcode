class Solution:
    def addDigits(self, num: int) -> int:
        
        
        while True:
            res = 0
            while num:
                num, d = divmod(num, 10)
                res += d
                
            x, _ = divmod(res, 10)
            if x == 0:
                break
            num = res
            
        return res