class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(current))
                return
            
            if open < n:
                current.append("(")
                backtrack(open + 1, closed)
                current.pop()
            
            if closed < open:
                current.append(")")
                backtrack(open, closed + 1)
                current.pop()
        
        backtrack(0, 0)
        return res