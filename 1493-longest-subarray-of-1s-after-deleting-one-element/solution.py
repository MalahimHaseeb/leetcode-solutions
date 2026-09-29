class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if 1 not in nums : return 0
        if 0 not in nums : return len(nums) - 1

        left = 0
        best = 0
        zero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1

                while zero > 1:
                    if nums[left] == 0:
                        zero -= 1
                    left +=1
            best = max(best, right - left + 1)
        
        return 0 if best == 0 else best - 1
