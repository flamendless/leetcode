class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        
        res = 200
        match = 0
        
        for idx in range(0, len(strs) - 1, 1):

            a, b = strs[idx], strs[idx + 1]

            i = 0
            d = min(len(a), len(b))
            while ((i < d) and a[i] == b[i]):
                i += 1
                match = idx
            res = min(res, i)
            
        return strs[match][:res]