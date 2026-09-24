class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, anchor in enumerate(nums):
            # if anchor is > 0, there is no solution
            if anchor > 0:
                break
            
            # skip dupes
            if i > 0 and anchor == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current = anchor + nums[l] + nums[r]
                if current > 0:
                    r -= 1
                elif current < 0:
                    l += 1
                else:
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip dupes
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
