class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = -float("inf")
        l = 0
        r = len(height) - 1
        
        while l <= r:
            n = min(height[l], height[r])
            highest = max(highest, n * (r - l))

            if height[l] < height[r]:

                l += 1
            else:
                r -= 1
                
        return highest
