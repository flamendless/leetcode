class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        
        for y in range(9):
            for x in range(9):
                c = board[y][x]
                if c == ".":
                    continue
                    
                k1 = (y, c)
                k2 = (c, x)
                k3 = (y // 3, x // 3, c)
                
                if (
                    (k1 in s) or
                    (k2 in s) or
                    (k3 in s)
                ):
                    return False
                
                s.add(k1)
                s.add(k2)
                s.add(k3)
                
        return True