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
        current = ""

        def backtrack(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            
            for c in phone[digits[i]]:
                backtrack(i + 1, current + c)
            
        if digits:
            backtrack(0, "")
        return res
