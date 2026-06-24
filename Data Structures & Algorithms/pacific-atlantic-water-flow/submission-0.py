class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific_path = [[False] * COLS for _ in range(ROWS)]
        atlantic_path = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, path):
            q = deque(source)
            while q:
                r, c = q.popleft()
                path[r][c] = True
                for dr, dc in directions:
                    new_row, new_col = dr + r, dc + c
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and
                        not path[new_row][new_col] and
                        heights[new_row][new_col] >= heights[r][c]
                    ):
                        q.append((new_row, new_col))

        
        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))
        
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pacific_path)
        bfs(atlantic, atlantic_path)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific_path[r][c] and atlantic_path[r][c]:
                    res.append([r, c])
        return res

            