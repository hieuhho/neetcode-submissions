class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(row, col, i):
            if row < 0 or row >= rows:
                return False
            if col < 0 or col >= cols:
                return False
            if (row, col) in visited:
                return False
            
            if i == len(word) -1 and board[row][col] == word[i]:
                return True
            if board[row][col] != word[i]:
                return False

            visited.add((row, col))
            found = (backtrack(row - 1, col, i + 1) or
            backtrack(row + 1, col, i + 1) or
            backtrack(row, col - 1, i + 1) or
            backtrack(row, col + 1, i + 1))
            visited.remove((row, col))
            if found:
                return True
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False

