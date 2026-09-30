class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows = {}

        for row in grid:
            key = tuple(row)
            rows[key] = rows.get(key,0) + 1

        count = 0
        
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += rows.get(col,0)
        
        return count
