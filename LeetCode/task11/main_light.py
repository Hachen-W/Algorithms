class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        maximum = 0
        while left_index < right_index:
            maximum = max(
                maximum,
                min(height[left_index], height[right_index]) * (right_index - left_index)
                )

            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return maximum
