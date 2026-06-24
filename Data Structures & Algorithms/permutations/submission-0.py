class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            for idx in range(i, len(path)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(i + 1, path)
                nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(0, nums)
        return res