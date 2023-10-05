class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        
        for i in range(len(nums) - 1):
            l = nums[i]
            r = nums[i + 1]
            
            if not (l <= r):
                inc = False
            elif not (r <= l):
                dec = False
                
        return inc or dec