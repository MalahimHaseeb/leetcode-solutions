class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        current = 1
        for i in range(n):
            result[i] = current
            current *= nums[i]
        
        current = 1

        for i in reversed(range(n)):
            result[i] *= current
            current *= nums[i]
        
        return result

        
