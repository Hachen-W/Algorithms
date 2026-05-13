from itertools import product
from typing import List


class Solution:
    def isValid(self, bracks: str) -> bool:
        len_bracks = len(bracks)
        bracks_opened = 0
        for index in range(len_bracks):
            if bracks[index] == '(':
                bracks_opened += 1
            if bracks[index] == ')':
                bracks_opened -= 1
            if bracks_opened < 0:
                return False
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        answer = ['(' * n + ')' * n]
        for states in product(range(n), repeat=n):
            if sum(states) == n:
                temp = ''
                for index in range(n):
                    temp += '(' + ')' * states[index]
                if self.isValid(temp):
                    answer.append(temp)
            if all([digit == 1 for digit in states]):
                break
        return answer


print(Solution().generateParenthesis(4))
