class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        third: int = len(nums) // 3
        counter: dict = {}
            
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
            
        return [
            k
            for k, v in counter.items()
            if v > third
        ]