class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        min_prod = 1
        max_prod = 1
        res = max(nums)
        for num in nums:
            tmp = min_prod
            min_prod = min(num, num * min_prod, num * max_prod)
            max_prod = max(num, num * tmp, num * max_prod)
            res = max(res, min_prod, max_prod)
        return res
