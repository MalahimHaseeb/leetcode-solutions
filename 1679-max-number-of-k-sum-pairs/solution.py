class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {}

        for x in nums:
            target  = k - x

            if seen.get(target,0) > 0:
                count +=1
                seen[target] -= 1
            else:
                seen[x] = seen.get(x,0) + 1
        
        return count
