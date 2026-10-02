class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(y / x)
        }

        for n in tokens:
            if n in op:
                stack.append(op[n](stack.pop(), stack.pop()))
            else:
                stack.append(int(n))
        return stack[0]