class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # add all treasure to a queue
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (new_row < 0 or new_col < 0 or
                    new_row >= ROWS or new_col >= COLS or
                    grid[new_row][new_col] != INF
                ):
                    continue
                grid[new_row][new_col] = grid[row][col] + 1
                q.append((new_row, new_col))
        
