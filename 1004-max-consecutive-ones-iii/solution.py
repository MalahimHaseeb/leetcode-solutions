class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if not nums or n < k:
            return 0 
        
        left  = zeros = best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros +=1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -=1
                
                left +=1
            best = max(best, right - left +1)
        
        return best
