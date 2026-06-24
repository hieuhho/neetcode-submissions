class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ###
        # add a path
        
        # if sum == target
        # path is correct, add to ans
        # if sum + current num > target
        # return

        # else 
        # add current num to path, and sum using backtrack
        # pop the current num
        ###

        ans = []

        def backtrack(start, path, total):
            if total == target:
                ans.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()
        backtrack(0, [], 0)
        return ans
