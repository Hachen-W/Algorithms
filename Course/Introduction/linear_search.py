class Solution:
    def linear_search(self, array: list[int], target: int) -> int:
        array_length = len(array)
        for index in range(array_length):
            if array[index] == target:
                return index
        return -1
