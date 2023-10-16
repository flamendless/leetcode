class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        if sl != tl:
            return False
        
        sd = {}
        td = {}
        
        for c in s:
            if c not in sd:
                sd[c] = 0
            sd[c] += 1
            
        for c in t:
            if c not in td:
                td[c] = 0
            td[c] += 1
            
        return sd == td