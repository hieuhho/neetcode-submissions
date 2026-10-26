class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, current):
            if i == len(nums):
                res.append(current.copy())
                return

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, current)
        
        backtrack(0, [])
        return res