class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        if len(arr) < 2:
            return True
        
        count = {}

        for num in arr:
            count[num] = count.get(num,0) + 1
        
        seen = set()

        for f in count.values():
            if f in seen:
                return False
            seen.add(f)
        
        return True
        
