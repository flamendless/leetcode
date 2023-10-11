class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # TLE
        """
        res = [] 
        for i, pos in enumerate(people):
            n = 0
            for start, end in flowers:
                if (pos >= start) and (pos <= end):
                    n += 1
            res.append(n)
        
        return res
        """

        d = {}
        for start, end in flowers:
            if start not in d:
                d[start] = 0
            if end + 1 not in d:
                d[end + 1] = 0
                
            d[start] += 1
            d[end + 1] -= 1
            
        sorted_p = sorted(people)[::-1]
        
        n = 0
        times = []
        for time in sorted(d):
            n += d[time]
            times.append((time, n))
            
        res = []
        for p in people:
            l = bisect_left(times, p, key=lambda x: x[0])
            if p not in d:
                l -= 1
            res.append(times[l][1])
        
        return res
            
            
            
            
            