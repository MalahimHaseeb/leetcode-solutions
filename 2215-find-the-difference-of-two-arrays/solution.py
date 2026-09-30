class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        val_s1 = set(nums1)
        va_s2 = set(nums2)

        return list(val_s1.difference(va_s2)) , list(va_s2.difference(val_s1))
