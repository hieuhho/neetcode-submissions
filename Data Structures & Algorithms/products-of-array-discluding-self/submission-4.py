class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [0] * len(nums) 
        forward[0] = 1
        backward = [0] * len(nums) 
        backward[-1] = 1
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]
        
        res = [0] * len(nums) 
        for i in range(len(nums)):
            res[i] = forward[i] * backward[i]
        return res

            