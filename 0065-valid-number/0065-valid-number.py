class Solution:
    def isNumber(self, s: str) -> bool:
        has_num = has_e = has_sign = has_dot = False
        
        for ch in s:
            if ch.isdigit():
                has_num = True
            elif ch.lower() == "e":
                if has_e or (not has_num):
                    return False
                has_e = True
                has_num = has_sign = has_dot = False
            elif (ch == "+") or (ch == "-"):
                if has_sign or has_num or has_dot:
                    return False
                has_sign = True
            elif ch == ".":
                if has_dot or has_e:
                    return False
                has_dot = True
            else:
                return False
        
        return has_num
        
        
        
        
        