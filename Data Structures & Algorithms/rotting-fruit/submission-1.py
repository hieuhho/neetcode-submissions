class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0
        time = 0

        # add all rotten
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):                     # the current rotting
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row < 0 or new_col < 0 or
                        new_row >= ROWS or new_col >= COLS or
                        grid[new_row][new_col] != 1
                    ):
                        continue
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col))        # new rotten, will process next time
                    fresh -= 1
            time += 1                                   # one iteration, can rot multiple
        
        return time if fresh == 0 else -1
