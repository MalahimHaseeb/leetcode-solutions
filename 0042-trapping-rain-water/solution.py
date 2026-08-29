class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water_trap = 0
        maxIndex = height.index(max(height))

        left_max = height[0]
        for  i in range(1, maxIndex):
            if height[i] > left_max:
                left_max = height[i]
            else:
                water_trap += left_max - height[i]
        
        right_max = height[-1]
        for i in range(len(height) - 2, maxIndex, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                water_trap += right_max - height[i]
        
        return water_trap


        
