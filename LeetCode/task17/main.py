from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            "0": "/",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        answer = [""]

        while len(digits) < 4:
            digits += "0"

        for symbol_1 in digits_to_letters[digits[0]]:
            for symbol_2 in digits_to_letters[digits[1]]:
                for symbol_3 in digits_to_letters[digits[2]]:
                    for symbol_4 in digits_to_letters[digits[3]]:
                        word = "".join([symbol for symbol in (symbol_1, symbol_2, symbol_3, symbol_4) if symbol != "/"])
                        answer.append(word)

        return answer[1:]


print(Solution().letterCombinations(""))
