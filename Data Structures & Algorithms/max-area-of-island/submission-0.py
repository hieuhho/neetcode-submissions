class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            current_area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row < 0 or new_col < 0 or
                        new_row >= ROWS or new_col >= COLS or
                        grid[new_row][new_col] == 0 or
                        (new_row, new_col) in visited 
                    ):
                        continue
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    current_area += 1
            return current_area
            

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    res = max(res, bfs(row, col))
        return res