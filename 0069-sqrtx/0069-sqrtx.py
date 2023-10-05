class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        n = 2
        while True:
            if n * n == x:
                return n
            if n * n > x:
                return floor(n) - 1
            n += 1