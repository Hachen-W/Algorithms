class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
            if len(s) == 0:
                return 0
        elif s[0] == '+':
            sign = 1
            s = s[1:]
            if len(s) == 0:
                return 0

        allowed_symbols = '0123456789'

        first_invalid = next((idx for idx, char in enumerate(s) if char not in allowed_symbols), None)
        if first_invalid is None:
            answer = int(s) * sign
        else:
            answer = int('0' + s[:first_invalid]) * sign

        if answer < -2**31:
            answer = -2**31
        if answer > 2**31 - 1:
            answer = 2**31 - 1

        return answer
