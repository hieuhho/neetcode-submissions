class Solution:
    def dp(self, houses):
        if len(houses) == 1: return houses
        profit = [0] * len(houses)
        profit[0] = houses[0]
        profit[1] = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            profit[i] = max(houses[i] + profit[i - 2], profit[i - 1])
        return profit

    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        rob1 = self.dp(nums[:-1])
        rob2 = self.dp(nums[1:])
        return max(rob1[-1], rob2[-1])



        