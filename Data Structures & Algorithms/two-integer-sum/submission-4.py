class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for ix, num in enumerate(nums):
            sub = target - nums[ix]
            if sub in diff:
                return [diff[sub], ix]
            else:
                diff[num] = ix
            print(sub, diff)        