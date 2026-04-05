from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_count = len(nums)
        for first in range(numbers_count):
            for second in range(first + 1, numbers_count):
                if nums[first] + nums[second] == target:
                    return [first, second]
