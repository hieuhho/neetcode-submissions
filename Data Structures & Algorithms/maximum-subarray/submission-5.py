class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = current = nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            largest = max(largest, current)
        return largest