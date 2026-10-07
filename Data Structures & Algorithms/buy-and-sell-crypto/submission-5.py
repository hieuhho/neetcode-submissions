class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in prices:
            
            res = max(res, i - buy)
            buy = min(buy, i)
        return res