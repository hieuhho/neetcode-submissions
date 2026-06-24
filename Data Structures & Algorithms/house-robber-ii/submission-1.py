class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: List[int]) -> int:
        start_1, start_2 = 0, 0
        for i in nums:
            new_max = max(i + start_1, start_2)
            start_1 = start_2
            start_2 = new_max
        return start_2