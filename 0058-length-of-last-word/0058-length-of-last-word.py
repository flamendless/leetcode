class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = [word.strip() for word in words if word.strip()]
        return len(words[-1])