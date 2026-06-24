class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        calc = {}
        for i in range(len(nums)):
            if nums[i] in calc:
                return [calc[nums[i]], i]
            remain = target - nums[i]
            calc[remain] = i
            
