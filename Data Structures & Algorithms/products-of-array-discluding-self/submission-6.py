class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        forward = [0] * n
        forward[0] = 1
        for i in range(1, n):
            forward[i] = forward[i - 1] * nums[i - 1]
        
        backward = [0] * n
        backward[-1] = 1
        for i in range(n - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = forward[i] * backward[i]
        return res
