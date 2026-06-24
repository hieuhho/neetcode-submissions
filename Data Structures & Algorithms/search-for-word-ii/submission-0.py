class TrieNode():
    def __init__(self):
        self.child = {}
        self.end = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        ans, visited = set(), set()

        def dfs(r, c, node, current_word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                board[r][c] not in node.child):
                return
            visited.add((r, c))

            node = node.child[board[r][c]]
            current_word += board[r][c]

            if node.end:
                ans.add(current_word)

            dfs(r - 1, c, node, current_word)
            dfs(r + 1, c, node, current_word)
            dfs(r, c- 1, node, current_word)
            dfs(r, c + 1, node, current_word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(ans)