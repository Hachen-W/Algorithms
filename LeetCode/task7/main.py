class Solution:
    def reverse(self, x: int) -> int:
        if not (x > -2**31 and x < 2**31 - 1):
            return 0

        if x > 0:
            sign = 1
        else:
            sign = -1

        answer = 0
        x *= sign
        while x != 0:
            answer *= 10
            answer += x % 10
            x //= 10

        if not (answer > -2**31 and answer < 2**31 - 1):
            return 0
        return answer * sign


print(Solution().reverse(-123))
