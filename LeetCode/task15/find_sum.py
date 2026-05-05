def find_sum(nums: list[int], sum_target: int) -> list[int]:
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


nums = [-1, -2, -7, 5]
nums.sort()
print(find_sum(nums, -2))
