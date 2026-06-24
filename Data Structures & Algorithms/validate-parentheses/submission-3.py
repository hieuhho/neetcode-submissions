class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        close_bracket_dict = dict([(value, key) for key, value in open_bracket_dict.items()])
    
        for i in s:
            if i in close_bracket_dict:
                if not stack or stack[-1] != close_bracket_dict[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return not stack