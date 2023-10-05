class Solution:
    res: List[List[int]] = None

    def rec_permute(
        self,
        data: List[int],
        i: int,
        length: int,
    ) -> List[int]:
        if i == length:
            self.res.append(list(data))
            return

        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            self.rec_permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.rec_permute(list(nums), 0, len(nums))
        return self.res