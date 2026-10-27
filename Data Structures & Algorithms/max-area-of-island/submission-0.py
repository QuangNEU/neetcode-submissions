class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            total = 1
            grid[r][c] = 0
            total += dfs(r+1, c)
            total += dfs(r-1, c)
            total += dfs(r, c+1)
            total += dfs(r, c-1)
            return total
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    res = max(dfs(r,c), res)
        return res