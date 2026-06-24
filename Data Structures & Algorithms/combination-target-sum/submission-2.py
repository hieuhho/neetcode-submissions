class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        current_list = []
        def dfs(i, current_list, total):
            if total == target:
                ans.append(current_list.copy())
                return

            if i >= len(nums) or total > target:
                return

            current_list.append(nums[i])
            dfs(i, current_list, total + nums[i])
            current_list.pop()
            dfs(i + 1, current_list, total)

        dfs(0, current_list, 0)
        return ans