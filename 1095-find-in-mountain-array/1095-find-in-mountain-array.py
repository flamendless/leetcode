# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak = None
        
        l = 1
        r = length - 2
        while l <= r:
            m = l + (r - l) // 2
            a = mountain_arr.get(m - 1)
            b = mountain_arr.get(m)
            c = mountain_arr.get(m + 1)
            
            if a < b < c:
                l = m + 1
            elif a > b > c:
                r = m - 1
            else:
                peak = m
                break
                
        l = 0
        r = peak
        while l <= r:
            m = l + (r - l) // 2
            v = mountain_arr.get(m)
            if v == target:
                return m
            if v < target:
                l = m + 1
            else:
                r = m - 1
                
        l = peak
        r = length - 1
        while l <= r:
            m = l + (r - l) // 2
            v = mountain_arr.get(m)
            if v == target:
                return m
            if v > target:
                l = m + 1
            else:
                r = m - 1
                
                
        return -1
                
        
        
        
        
        