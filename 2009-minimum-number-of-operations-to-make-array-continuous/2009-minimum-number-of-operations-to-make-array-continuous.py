class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        unique = list(set(nums))
        unique.sort()
        
        res = 1
        l = 0
        r = 0
        
        unique_length = len(unique)
        
        while r < unique_length:
            while (
                (r < unique_length) and
                (unique[r] <= (unique[l] + length - 1))
            ):
                res = max(res, r - l + 1)
                r += 1
                
            l += 1
        
        return length - res
            
        