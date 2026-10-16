class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0

        fruits = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruits += 1
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fruits > 0:
            rot = False
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        for dr, dc in dirs:
                            row, col = r + dr, c + dc
                            if (row in range(rows) and
                                col in range(cols) and
                                grid[row][col] == 1
                            ):
                                grid[row][col] = 3
                                fruits -= 1
                                rot = True

            if not rot:
                return -1
        
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            
            time += 1
        return time