class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # find rotated point
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        rotated = l

        # find the half the target is in
        l, r = 0, len(nums) - 1
        if nums[rotated] <= target and target <= nums[r]:
            l = rotated
        else:
            r = rotated - 1
        
        # binary search on the half
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1