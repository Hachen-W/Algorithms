import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        subarray_size = numRows * 2 - 2
        string_length = len(s)
        subarray_count = math.ceil(string_length / subarray_size)
        subarray_index = 0
        answer = [[] for _ in range(subarray_count)]
        index = 0
        while index < string_length:
            if index % subarray_count == 0 or \
                    index % subarray_count == subarray_count - 1:
                answer[subarray_index].append(s[index])
                subarray_index += 1
                subarray_index = subarray_index % subarray_count
            else:
                answer[subarray_index].append(s[index])
                answer[subarray_index].append(s[index + 1])
                subarray_index += 1
                index += 1
            index += 1
        return answer


print(Solution().convert("PAYPALISHIRING", 3))
