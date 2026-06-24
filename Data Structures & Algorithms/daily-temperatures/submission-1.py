class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for idx, current_tempt in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_tempt:
                ans[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return ans
