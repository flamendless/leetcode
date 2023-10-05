class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res: int = 0
        for c in s:
            res ^= ord(c)
        for c in t:
            res ^= ord(c)
        return chr(res)

        