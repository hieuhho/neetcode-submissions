class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0] * len(height) , [0] * len(height)
        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        maxRight[- 1] = height[- 1]
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        res = 0
        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return res
