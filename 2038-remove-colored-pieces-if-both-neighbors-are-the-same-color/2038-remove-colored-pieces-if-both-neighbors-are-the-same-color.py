class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        x = 0
        y = 0
        
        for i in range(1, len(colors) - 1):
            a = colors[i - 1]
            b = colors[i]
            c = colors[i + 1]
            
            if a == b == c:
                if a == "A":
                    x += 1
                else:
                    y += 1
            
        return x > y