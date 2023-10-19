class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            ss = []
            tt = []

            sl = len(s)
            tl = len(t)
            l = max(sl, tl)

            for i in range(l):
                if i < sl:
                    if s[i] == "#":
                        if ss:
                            ss.pop()
                    else:
                        ss.append(s[i])

                if i < tl:
                    if t[i] == "#":
                        if tt:
                            tt.pop()
                    else:
                        tt.append(t[i])

            return "".join(ss) == "".join(tt)


                