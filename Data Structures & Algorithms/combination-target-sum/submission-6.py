class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            for j in range(i, len(nums)):
                currSum = total + nums[j]
                if currSum > target:
                    return
                current.append(nums[j])
                backtrack(j, current, currSum)
                current.pop()
            
        backtrack(0, [], 0)
        return res