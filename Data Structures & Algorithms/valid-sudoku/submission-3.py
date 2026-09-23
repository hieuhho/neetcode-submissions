class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = {}, {}, {}
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in rows.get(r, ()) or
                    val in cols.get(c, ()) or
                    val in squares.get((r//3, c//3), ())
                ):
                    return False
                rows.setdefault(r, set()).add(val)
                cols.setdefault(c, set()).add(val)
                squares.setdefault((r//3, c//3), set()).add(val)
        return True