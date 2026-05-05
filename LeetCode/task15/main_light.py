class Solution:
    def find_sum(self, nums: list[int], sum_target: int) -> list[int]:
        left_index = 0
        right_index = len(nums) - 1
        
        while nums[left_index] + nums[right_index] != sum_target:
            if abs(nums[left_index] + nums[right_index]) < abs(sum_target):
                left_index += 1
            else:
                right_index -= 1
            if left_index == right_index:
                return None

        if nums[left_index] + nums[right_index] != sum_target:
            return None
        return [left_index, right_index]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_length = len(nums)
        data = []
        
        for start_index in range(nums_length - 2):
            addition = self.find_sum(nums[start_index + 1:], -nums[start_index])
            if addition is None:
                continue
            triple_cur = [
                nums[start_index],
                nums[addition[0] + start_index + 1],
                nums[addition[1] + start_index + 1]
            ]
            data.append(triple_cur)

        unique_data = []
        for item in data:
            if item not in unique_data:
                unique_data.append(item)

        return unique_data


print(Solution().threeSum([-1,0,1,2,-1,-4]))
