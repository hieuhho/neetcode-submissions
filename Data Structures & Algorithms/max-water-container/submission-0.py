class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max_height = 0
        while l < r:
            height = (r - l) * min(heights[l], heights[r])
            max_height = max(max_height, height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_height
