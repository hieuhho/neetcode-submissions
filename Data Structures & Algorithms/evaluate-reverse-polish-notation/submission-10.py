class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for i in tokens:
            if i == "+":
                ans.append(ans.pop() + ans.pop())
            elif i == "-":
                a = ans.pop()
                b = ans.pop()
                ans.append(b - a)
            elif i == "*":
                ans.append(ans.pop() * ans.pop())
            elif i == "/":
                a = ans.pop()
                b = ans.pop()
                ans.append(int(b / a))
            else:
                ans.append(int(i))
        return ans[0]