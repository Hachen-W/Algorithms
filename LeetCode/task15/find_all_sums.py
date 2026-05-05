def find_all_sums(nums: list[int], sum_target: int) -> list[int]:
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


nums = [-1, -2, -7, 5]
nums.sort()
print(find_all_sums(nums, -2))
