class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length: int = len(nums)

        prefix_left: List[int] = [0] * length
        prefix_right: List[int] = [0] * length

        prefix_left[0] = 1
        prefix_right[length - 1] = 1

        for i in range(1, length):
            prefix_left[i] = nums[i - 1] * prefix_left[i - 1]

        for i in range(length - 2, -1, -1):
            prefix_right[i] = nums[i + 1] * prefix_right[i + 1]

        res: List[int] = [0] * length
        for i in range(length):
            res[i] = prefix_left[i] * prefix_right[i]

        return res