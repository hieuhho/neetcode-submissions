class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        for r in range(k, len(nums) + 1):
            ans.append(max(nums[l:r]))
            l += 1
            r += 1
        return ans