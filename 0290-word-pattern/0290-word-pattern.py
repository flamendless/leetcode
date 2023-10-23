class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        
        if len(ss) != len(pattern):
            return False
        
        d = {}
        d2 = {}
        
        for i in range(len(ss)):
            p = pattern[i]
            w = ss[i]
            
            if (p in d) and (d[p] != w):
                return False
            
            if (w in d2) and (d2[w] != p):
                return False
            
            d[p] = w
            d2[w] = p
                
        return True