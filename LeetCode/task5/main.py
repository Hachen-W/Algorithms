class Solution:
    def isPalindrome(self, s: str):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        for substring_length in range(s_length):
            for index_finish in range(s_length - 1, substring_length - 1, -1):
                if self.isPalindrome(
                        s[index_finish - substring_length: index_finish + 1]
                        ):
                    answer = s[
                        index_finish - substring_length: index_finish + 1
                        ]
                    break
        return answer
