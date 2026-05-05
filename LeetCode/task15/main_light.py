class Solution:
    def find_all_sums(self, nums: list[int], sum_target: int) -> list[int]:
        left_index = 0
        right_index = len(nums) - 1
        answer = []
        
        while left_index != right_index:
            if nums[left_index] + nums[right_index] == sum_target:
                answer.append([nums[left_index], nums[right_index]])
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

        unique_data = []
        for item in data:
            if item not in unique_data:
                unique_data.append(item)

        return unique_data


print(Solution().threeSum([-1,0,1,2,-1,-4]))
