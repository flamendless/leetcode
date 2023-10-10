class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m - 1
        r = n - 1
        cur = m + n - 1
        
        while r >= 0:
            if l >= 0 and nums1[l] > nums2[r]:
                nums1[cur] = nums1[l]
                l -= 1
            else:
                nums1[cur] = nums2[r]
                r -= 1
            cur -= 1
        