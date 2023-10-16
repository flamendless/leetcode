class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1]
        prev = 1
        for i in range(1, rowIndex + 1):
            n = prev * (rowIndex - i + 1) // i
            res.append(n)
            prev = n
            
        return res