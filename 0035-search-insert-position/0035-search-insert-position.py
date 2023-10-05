class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        
        i = 0

        while True:
            if nums[i] == target:
                return i
            
            if nums[i] > target:
                return i
            
            i += 1
