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
        index = 0
        for curRow in range(numRows):
            for curCol in range(0, math.ceil(string_length / subarray_size) + 1, zigzagWidth):
                if curCol - offset > 0 and offset != zigzagWidth and offset != 0:
                    answer[curCol][curRow] = s[index]
                    index += 1
                answer[curCol][curRow] = s[index]
                index += 1
                offset -= 1


print(Solution().convert("PAYPALISHIRING", 3))
