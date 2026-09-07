class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if d > n:
            return -1

        @lru_cache(None)
        def dp(i, days):
            if days == 1:
                return max(jobDifficulty[i:])

            ans = math.inf
            mx = 0

            for j in range(i, n - days + 1):
                mx = max(mx, jobDifficulty[j])
                ans = min(ans, mx + dp(j + 1, days - 1))

            return ans

        return dp(0, d)
