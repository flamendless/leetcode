class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        q = []
        
        open_par = ["(", "{", "["]
        close_par = [")", "}", "]"]
        
        for c in s:
            if c in open_par:
                q.append(c)
                
            if c in close_par:
                if not q:
                    return False
                d = q.pop()
                x = close_par.index(c)
                y = open_par.index(d)
                
                if x != y:
                    return False
                
        if q:
            return False
                
        return True
            