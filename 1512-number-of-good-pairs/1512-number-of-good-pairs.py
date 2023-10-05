class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res: int = 0
        d: dict[int, int] = {}
            
        for i in nums:
            if i in d:
                res += d[i]
                d[i] += 1
                
            else:
                d[i] = 1
                
        return res