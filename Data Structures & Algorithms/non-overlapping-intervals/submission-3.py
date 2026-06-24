class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        if not intervals:
            return ans
        intervals.sort(key=lambda x:x[0])
        max_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= max_end:
                max_end = e
            else:
                ans += 1
                max_end = min(max_end, e)

        return ans