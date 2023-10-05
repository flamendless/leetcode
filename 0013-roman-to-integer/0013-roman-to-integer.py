class Solution:
    def romanToInt(self, s: str) -> int:
        d: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res: int = 0
        l: int = len(s)

        i = 0
        while i < l:
            a = s[i]
            if (i + 1) < l:
                b = s[i + 1]
                if d[a] < d[b]:
                    res += d[b] - d[a]
                    i += 2
                    continue
            res += d[a]
            i += 1

        return res