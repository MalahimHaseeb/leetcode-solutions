class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        low  = 0
        high = len(nums)-1

        while low <= high:
            mid = int(low + (high-low) /2)

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                low = mid + 1
            
            else:
                high = mid-1
        
        return -1
        
        

          
             
        
        
       



        
