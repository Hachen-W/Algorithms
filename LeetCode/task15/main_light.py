class Solution:
    def find_all_sums(self, nums: list[int], sum_target: int) -> list[int]:
        left_index = 0
        right_index = len(nums) - 1
        answer = []
        
        while left_index != right_index:
            if (nums[left_index] + nums[right_index] == sum_target and 
                    (nums[left_index], nums[right_index]) not in answer
                    ):
                answer.append((nums[left_index], nums[right_index]))
            if abs(nums[left_index] + nums[right_index]) < abs(sum_target):
                left_index += 1
            else:
                right_index -= 1

        return answer

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_length = len(nums)
        data = []
        
        for start_index in range(nums_length - 2):
            if start_index - 1 >= 0 and nums[start_index - 1] == nums[start_index]:
                continue
            addition = self.find_all_sums(nums[start_index + 1:], -nums[start_index])
            if len(addition) == 0:
                continue
            for addition_first, addition_second in addition:
                triple_cur = [
                    nums[start_index],
                    addition_first,
                    addition_second
                ]
                data.append(triple_cur)

        return data


print(Solution().threeSum([0, 0, 0, 0]))
