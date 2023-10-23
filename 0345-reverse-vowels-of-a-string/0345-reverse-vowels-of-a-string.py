class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        
        vowels = ["a", "e", "i", "o", "u"]
        
        l = 0
        r = len(ss) - 1
        
        while l < r:
            cl = ss[l].lower()
            cr = ss[r].lower()
            
            a = cl in vowels
            b = cr in vowels
            
            if not a:
                l += 1
                
            if not b:
                r -= 1
                
            if a and b:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
                
        return "".join(ss)