import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound is max(piles)
        # lower bound is 1
        # binary search between 1 & upperbound
        largest_k = max(piles)
        lowest_k = 1
        ans = largest_k
        while lowest_k <= largest_k:
            mid_k = lowest_k + ((largest_k - lowest_k) // 2)
            hours = sum(math.ceil(pile / mid_k) for pile in piles)
            if hours <= h:
                ans = min(ans, mid_k)
                largest_k = mid_k - 1
            else:
                lowest_k = mid_k + 1
        return ans