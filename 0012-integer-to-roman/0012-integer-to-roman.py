class Solution:
    def intToRoman(self, num: int) -> str:
        d: list[tuple[str, int]] = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]

        # res: list[str] = []
        res: str = ""

        for k, v in d:
            if num // v:
                r = num // v
                # res.append(k * r)
                res += k * r
                num = num % v

        # return "".join(res)
        return res