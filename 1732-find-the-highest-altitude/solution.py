class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        best = 0

        for g in gain:
            altitude += g
            best = max(best, altitude)
        
        return best
