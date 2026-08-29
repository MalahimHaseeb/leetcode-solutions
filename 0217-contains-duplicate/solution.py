class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if None in nums:
            return False
        
        has_duplicate = len(nums) != len(set(nums))
        return has_duplicate
    
        
