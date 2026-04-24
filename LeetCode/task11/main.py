class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_length = len(height)
        maximum = 0
        for first_index in range(height_length):
            for second_index in range(first_index + 1, height_length):
                maximum = max(
                    maximum,
                    min(height[first_index], height[second_index]) * (second_index - first_index)
                    )
        return maximum
