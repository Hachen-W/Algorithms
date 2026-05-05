class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_length = len(nums)
        answer = []
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                for third_index in range(second_index + 1, nums_length):
                    triple_cur = [
                        nums[first_index],
                        nums[second_index],
                        nums[third_index]
                        ]
                    if sum(triple_cur) == 0 and triple_cur not in answer:
                        answer.append(sorted(triple_cur))
        unique_data = []
        for item in answer:
            if item not in unique_data:
                unique_data.append(item)
        return unique_data


print(Solution().threeSum([-1,0,1,2,-1,-4]))
