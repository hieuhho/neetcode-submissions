class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            gain = prices[i] - lowest
            profit = max(profit, gain)
            
            
        return profit
            