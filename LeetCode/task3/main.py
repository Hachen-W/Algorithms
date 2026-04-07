class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        answer = 0

        for symbol in s:
            if symbol in current_string:
                current_string = current_string.split(symbol)[1] + symbol
            else:
                current_string += symbol
            if answer < len(current_string):
                answer = len(current_string)

        return answer
