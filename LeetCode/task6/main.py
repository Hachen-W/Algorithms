import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        stringLength = len(s)
        zigzagFullCount = math.floor(string_length / subarray_size)
        zigzagWidth = numRows - 1
        zigzagLastWidth = stringLength % (numRows * 2 - 2)
        if zigzagLastWidth == 0:
            zigzagLastWidth = 0
        elif zigzagLastWidth <= numRows:
            zigzagLastWidth = 1
        else:
            zigzagLastWidth = 1 + zigzagLastWidth - numRows
        answer = [[0 * numRows] for _ in range(zigzagWidth * zigzagFullCount + zigzagLastWidth)]


print(Solution().convert("PAYPALISHIRING", 3))
