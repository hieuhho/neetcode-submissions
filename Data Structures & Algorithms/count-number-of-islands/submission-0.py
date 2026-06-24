class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        check_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in check_dir:
                    new_row, new_col = dr + row, dc + col
                    if (new_row < 0 or new_col < 0 or
                        new_row >= rows or new_col >= cols or
                        grid[new_row][new_col] == "0" or
                        (new_row, new_col) in visited
                    ):
                        continue
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        return res


