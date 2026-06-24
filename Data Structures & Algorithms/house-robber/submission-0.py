class Solution:
    def rob(self, nums: List[int]) -> int:
        start_1, start_2 = 0, 0
        for num in nums:
            temp = max(start_1 + num, start_2)
            start_1 = start_2
            start_2 = temp
        return start_2