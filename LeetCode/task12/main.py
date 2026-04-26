class Solution:
    def intToRoman(self, number: int) -> str:
        numerals_Roman = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            }
        items = list(numerals_Roman.items())
        digits_count = len(str(number))
        answer = ""
        for number_order in range(digits_count):
            digit_current = (number // (10 ** number_order)) % 10
            if digit_current == 0:
                continue
            elif digit_current == 4:
                number_current = digit_current * 10 ** number_order
                for i, (key, value) in enumerate(items):
                    if value - items[i+1][1] == number_current:
                        answer = items[i+1][0] + key + answer
                        break
            elif digit_current == 9:
                number_current = digit_current * 10 ** number_order
                for i, (key, value) in enumerate(items):
                    if value - items[i+2][1] == number_current:
                        answer = items[i+2][0] + key + answer
                        break
            else:
                number_current = digit_current * 10 ** number_order
                for key, value in numerals_Roman.items():
                    if value == number_current:
                        answer = key + answer
                        break
                    elif value < number_current:
                        answer = key + self.intToRoman(number_current - value) + answer
                        break
        return answer


checker = Solution()
print(checker.intToRoman(3749))
