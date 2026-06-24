from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l = r = 0

        # keep the queue in decreasing order
        while r < len(nums):
            # pop smaller values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # resize window, q[0] is always the largest but we have to resize due to k
            if q[0] < l:
                q.popleft()

            # when we have a valid k window, add q[0] then move l forward
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        return ans