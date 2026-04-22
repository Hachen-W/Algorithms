class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        string_index = 0
        string_length = len(string)
        pattern_length = len(pattern)
        for pattern_index in range(pattern_length):
            if pattern[pattern_index] == '*':
                continue
            elif string_index == string_length:
                return False
            elif pattern[pattern_index] == '.':
                if pattern_index >= string_length:
                    return False
                if pattern_index + 1 < pattern_length and pattern[pattern_index + 1] == '*':
                    return True
            elif pattern_index + 1 != pattern_length and pattern[pattern_index + 1] == '*':
                while string_index < string_length and string[string_index] == pattern[pattern_index]:
                    string_index += 1
                continue
            elif pattern[pattern_index] != string[string_index]:
                return False
            string_index += 1
        if string_index != string_length:
            return False
        return True


print(Solution().isMatch('mississippi', 'mis*is*p*.'))
