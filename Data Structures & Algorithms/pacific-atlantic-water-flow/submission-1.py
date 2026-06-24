class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific_path = set()
        atlantic_path = set()

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific_path, heights[0][c])                  # iterate the top row
            dfs(ROWS - 1, c, atlantic_path, heights[ROWS - 1][c])   # iterate the bottom row

        for r in range(ROWS):
            dfs(r, 0, pacific_path, heights[r][0])                  # iterate the left col
            dfs(r, COLS - 1, atlantic_path, heights[r][COLS - 1])   # iterate the right col
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_path and (r, c) in atlantic_path:
                    res.append([r, c])
        return res

            