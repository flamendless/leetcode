class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = len(nums) // 2
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            
        for k, v in d.items():
            if v > t:
                return k
            
        