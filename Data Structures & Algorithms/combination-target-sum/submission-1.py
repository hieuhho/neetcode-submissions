class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, current, total):
            if total == target:
                ans.append(current.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            # include nums[i]
            current.append(nums[i])
            dfs(i, current, total + nums[i])

            # ignore nums[i]
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return ans