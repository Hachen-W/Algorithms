class Solution:
    def hasDuplicate(self, s: str) -> bool:
        used_symbols = set()
        for symbol in s:
            if symbol in used_symbols:
                return True
            used_symbols.add(symbol)
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        answer = [0, 0]
        for start in range(length):
            for finish in range(start, length):
                temp = s[start: finish + 1]
                if not self.hasDuplicate(temp) and len(temp) > answer[1]:
                    answer[0] = temp
                    answer[1] = len(temp)
        return answer[1]
