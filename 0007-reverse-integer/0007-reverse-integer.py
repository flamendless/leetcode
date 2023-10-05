class Solution:
    def reverse(self, x: int) -> int:
        from math import copysign
        sign: int = int(copysign(1, x))
        res: int = 0
        x = abs(x)

        while (x > 0):
            res *= 10
            res += (x % 10)
            x //= 10
            
        res *= sign

        if (
            (res < (-(2 ** 31))) or
            (res >= ((2 ** 31) - 1))
        ):
            return 0

        return res