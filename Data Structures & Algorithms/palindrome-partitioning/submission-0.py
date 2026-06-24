class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []

        def backtrack(i):
            if i >= len(s):
                res.append(current.copy())
                return
            
            for j in range(i, len(s)):
                if self.valid_palindrome(s, i, j):
                    current.append(s[i:j+1])
                    backtrack(j + 1)
                    current.pop()
        backtrack(0)
        return res

        
    def valid_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True