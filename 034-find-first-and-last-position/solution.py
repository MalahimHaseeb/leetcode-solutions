class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def combined_logic(isFirst:bool) -> int:
            low, high = 0, len(nums) - 1
            bound = -1

            while low <= high:
                mid = low + (high-low) // 2

                if nums[mid] == target:
                    bound = mid
                    
                    if isFirst:
                        high = mid -1
                    else:
                        low = mid+1
                
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid - 1
            
            return bound
        
        first_po = combined_logic(isFirst=True)
        last_pos = combined_logic(isFirst=False)

        return [first_po, last_pos]

        
