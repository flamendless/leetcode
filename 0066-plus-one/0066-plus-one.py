class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        c = 0
        while i >= 0:

            c = 0
            if digits[i] == 9:
                c = 1
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
            
        if c:
            digits.insert(0, c)
                
        return digits