class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif two_sum < target:
                    j += 1
                else:
                    k -= 1
        return ans