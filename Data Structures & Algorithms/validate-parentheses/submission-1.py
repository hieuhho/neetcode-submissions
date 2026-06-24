class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in parentheses:
                if stack and parentheses[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
