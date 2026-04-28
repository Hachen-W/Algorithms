class Solution:
    def romanToInt(self, number_Roman: str) -> int:
        numerals_Roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        answer = 0

        number_Roman = number_Roman.replace("IV", "IIII").replace("IX", "VIIII")
        number_Roman = number_Roman.replace("XL", "XXXX").replace("XC", "LXXXX")
        number_Roman = number_Roman.replace("CD", "CCCC").replace("CM", "DCCCC")

        for symbol in number_Roman:
            answer += numerals_Roman[symbol]

        return answer
