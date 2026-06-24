class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, current):
            if len(current) == len(digits):
                res.append("".join(current))
                return
            
            for l in phone[digits[i]]:
                current.append(l)
                backtrack(i + 1, current)
                current.pop()
        
        if digits:
            backtrack(0, [])
        return res