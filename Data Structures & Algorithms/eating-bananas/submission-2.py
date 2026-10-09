class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            
            # calc eating time for k
            k = 0
            for p in piles:
                k += math.ceil(float(p) / mid)
            
            # shrink to find minimum speek k
            if k <= h:
                res = mid
                r = mid - 1
            # too slow, increase speed k and search starting from mid
            else:
                l = mid + 1
        return res 