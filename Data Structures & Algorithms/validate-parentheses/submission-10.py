class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if stack and c in parentheses:
                if parentheses[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
                
        return len(stack) == 0
