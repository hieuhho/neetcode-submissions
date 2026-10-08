class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                result[stack_idx] = i - stack_idx
            stack.append((i, t))
        return result
