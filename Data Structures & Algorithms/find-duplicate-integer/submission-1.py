class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = nums[0]
        f = nums[nums[0]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]
            # break when s == f
        
        f = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return s

