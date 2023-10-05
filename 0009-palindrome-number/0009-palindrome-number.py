class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s: str = str(x)
        i: int = 0
        j: int = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1

        return True