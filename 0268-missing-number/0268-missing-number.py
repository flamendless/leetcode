class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        prev = None
        nums.sort()
        if nums[0] != 0:
            return 0
        
        for n in nums:
            if (prev is not None) and (prev + 1 != n):
                return prev + 1
            
            prev = n
            
        return len(nums)
            