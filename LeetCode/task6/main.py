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
        numCols = zigzagWidth * zigzagFullCount + zigzagLastWidth
        answer = [[0 * numRows] for _ in range(numCols)]

        offset = zigzagWidth
        for curRow in range(numRows):
            for curCol in range(math.ceil(string_length / subarray_size) + 1):
                pass



print(Solution().convert("PAYPALISHIRING", 3))
