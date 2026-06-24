class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        def dfs(i, total):
            if total > target or i == len(nums):
                return False
            if total == target:
                return True
    
            take = dfs(i + 1, total + nums[i])
            skip = dfs(i + 1, total)
            return take or skip

        return dfs(0, 0)