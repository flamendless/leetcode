class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        if not nums:
            return res
        
        length = len(nums)

        l = 0
        r = 0
        
        while (l < length) and (r < length):
            while (
                ((r + 1) < length) and
                ((nums[r] + 1) == (nums[r + 1]))
            ):
                r += 1
                
            ln = nums[l]
            rn = nums[r]
            if ln == rn:
                res.append(str(ln))
            else:
                res.append(f"{ln}->{rn}")

            r += 1
            l = r
        
        return res