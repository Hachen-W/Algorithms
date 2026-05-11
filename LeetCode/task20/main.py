class Solution:
    def isValid(self, s: str) -> bool:
        brackets_opened = []
        bracket_correspond = {
            '(': ')',
            '[': ']',
            '{': '}'
            }
        for bracket in s:
            if bracket in '([{':
                brackets_opened.append(bracket)
            else:
                if len(brackets_opened) == 0:
                    return False
                last = brackets_opened.pop()
                if bracket_correspond[last] != bracket:
                    return False
        return len(brackets_opened) == 0
