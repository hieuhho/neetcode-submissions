class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                grid[r][c] == 0 or (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            left = dfs(r - 1, c)
            right = dfs(r + 1, c)
            up = dfs(r, c - 1)
            down = dfs(r, c + 1)
            return 1 + left + right + up + down
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(res, dfs(row, col))
        return res            