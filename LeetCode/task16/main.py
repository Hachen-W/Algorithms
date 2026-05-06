from typing import List


class Solution:
    def find_sum_two_pointers(self, nums: List[int], start_index: int, target: int) -> int:
        left_index = start_index + 1
        right_index = len(nums) - 1
        answer = None

        while left_index != right_index:
            left_number = nums[left_index]
            right_number = nums[right_index]

            if answer is None or abs(answer - target) > abs(left_number + right_number - target):
                answer = left_number + right_number

            if left_number + right_number < target:
                left_index += 1
            else:
                right_index -= 1

        return answer

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = None
        nums_length = len(nums)
        nums.sort()

        for start_index in range(nums_length - 2):
            answer_cur = nums[start_index]
            answer_cur += self.find_sum_two_pointers(nums, start_index, target - nums[start_index])
            if answer is None or abs(answer_cur - target) < abs(answer - target):
                answer = answer_cur

        return answer


if __name__ == '__main__':
    nums = [0,1,2]
    target = 0
    print(Solution().threeSumClosest(nums, target))
