class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        h = 2 ** 31 - 1
        l = -2 ** 31

        s1 = -1 if dividend < 0 else 1
        s2 = -1 if divisor < 0 else 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        res = len(range(0, dividend - divisor + 1, divisor))
        if s1 == -1 or s2 == -1:
            res = -res
        if s1 == s2:
            res = abs(res)

        return max(l, min(res, h))
