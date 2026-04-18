import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        string_length = len(s)
        zigzag_symbols = numRows * 2 - 2
        zigzag_count = math.ceil(string_length / zigzag_symbols)
        answer = [[0] * zigzag_count * 2 for _ in range(numRows)]

        row_index = 0
        column_index = 0
        direction = 1
        for zigzag_symbol in range(string_length):
            answer[row_index][column_index] = s[zigzag_symbol]
            if row_index == numRows - 1 or (row_index == 1 and direction == -1):
                direction = direction * (-1)
                column_index += 1
                if row_index == 1 and direction == 1:
                    row_index = 0
                    continue
            row_index += direction

        answer_str = ''
        for cur_row in range(numRows):
            for cur_col in range(zigzag_count * 2):
                if answer[cur_row][cur_col] != 0:
                    answer_str += answer[cur_row][cur_col]
        return answer_str


print(Solution().convert("ABCDE", 2))
