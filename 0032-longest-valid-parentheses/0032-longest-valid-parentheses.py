class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]
        highest = 0

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack.append(i)
                continue

            l = stack.pop()
            if not stack:
                stack.append(i)
                continue

            highest = max(highest, i - stack[-1])

        return highest
                    
                    