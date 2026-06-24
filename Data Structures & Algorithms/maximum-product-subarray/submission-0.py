class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        current_max, current_min = 1, 1

        for n in nums:
            tmp_max = current_max
            current_max = max(n * current_max, n * current_min, n)
            current_min = min(n * tmp_max, n * current_min, n)
            ans = max(ans, current_max, current_min)
        return ans