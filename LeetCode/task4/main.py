class Solution:
    def findMedianSortedArrays(
            self, nums1: list[int], nums2: list[int]
            ) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        nums_before_median = (nums1_length + nums2_length) // 2
        nums1_index = 0
        nums2_index = 0
        median_prev = 0
        median = 0
        for _ in range(nums_before_median + 1):
            median_prev = median
            if nums1_index == nums1_length or \
                    (nums2_index < nums2_length) and \
                    (nums1[nums1_index] > nums2[nums2_index]):
                median = nums2[nums2_index]
                nums2_index += 1
            else:
                median = nums1[nums1_index]
                nums1_index += 1

        if (nums1_length + nums2_length) % 2 == 0:
            return (median_prev + median) / 2
        else:
            return median


solution = Solution()
median = solution.findMedianSortedArrays(
    list(map(int, input().split())), list(map(int, input().split()))
    )
print(median)
