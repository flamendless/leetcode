class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = {}

        for n in nums:
            if n not in found:
                found[n] = 0
            found[n] += 1

        for a, b in found.items():
            if b == 1:
                return a

        