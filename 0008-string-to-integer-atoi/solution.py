class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        i = 0
        sign = 1

       
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0

     
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        result = sign * num

        if result < -2**31:
            return -2**31

        if result > 2**31 - 1:
            return 2**31 - 1

        return result
