from typing import List


class Solution:
    def twoSum(self, nums: List[int], index_start: int, target: int) -> List[List[int]]:
        left = index_start
        right = len(nums) - 1
        answer = []
        while left != right:
            if nums[left] + nums[right] == target:
                answer.append([left, right])
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return answer

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        length_nums = len(nums)
        nums.sort()
        for index_1 in range(length_nums - 3):
            if index_1 > 0 and nums[index_1 - 1] == nums[index_1]:
                continue
            for index_2 in range(index_1 + 1, length_nums - 2):
                additional = self.twoSum(nums, index_2 + 1, target - nums[index_1] - nums[index_2])
                for index_3, index_4 in additional:
                    if sum(
                            [nums[index_1], nums[index_2],
                            nums[index_3], nums[index_4]]
                            ) == target:
                        answer.append([
                            nums[index_1], nums[index_2],
                            nums[index_3], nums[index_4]
                            ])
        unique_data = []
        for item in answer:
            if item not in unique_data:
                unique_data.append(item)
        return unique_data


nums = [2,2,2,2,2]
target = 8
print(Solution().fourSum(nums, target))
