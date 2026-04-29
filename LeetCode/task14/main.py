from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix

        min_length = len(strs[0])
        for word in strs:
            min_length = min(min_length, len(word))

        prefix_length = 0
        for cur_length in range(1, min_length + 1):
            prefix_cur = strs[0][:cur_length]
            prefix_length += 1
            for word in strs:
                if not (word[:cur_length] == prefix_cur):
                    prefix_length -= 1
                    return prefix
            prefix = prefix_cur

        return prefix


strs = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(strs))
