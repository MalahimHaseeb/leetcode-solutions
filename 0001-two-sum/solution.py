class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            curr = num
            rem = target - curr 
            
            if rem in nums:
                j = nums.index(rem)
                if i != j: 
                    return [i, j]
        
