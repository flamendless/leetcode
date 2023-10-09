class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        res = [-1, -1]
        l_found = r_found = False

        while l <= r:
            a = nums[l]
            b = nums[r]

            if not l_found and a == target:
                res[0] = l
                l_found = True

            if not r_found and b == target:
                res[1] = r
                r_found = True

            if l_found and r_found:
                break

            if not l_found:
                l += 1

            if not r_found:
                r -= 1

        return res
