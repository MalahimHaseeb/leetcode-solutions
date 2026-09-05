class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        if len(nums) == 2:
            return [nums, nums[::-1]]

        results = []
        totalAllow = 1
        for x in range(1, len(nums) + 1):
            totalAllow *= x

        nums.sort()
        results.append(nums[:])

        i = 1
        while i < totalAllow:
            k = -1
            for j in range(len(nums) - 2, -1, -1):
                if nums[j] < nums[j + 1]:
                    k = j
                    break
            
            l = -1
            for j in range(len(nums) - 1, k, -1):
                if nums[j] > nums[k]:
                    l = j
                    break
            
            nums[k], nums[l] = nums[l], nums[k]
            
            nums[k + 1:] = reversed(nums[k + 1:])
            
            results.append(nums[:])
            i += 1
            
        return results
