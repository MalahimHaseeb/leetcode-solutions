class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        sorted_data = sorted(nums1)
        return statistics.median(sorted_data)
