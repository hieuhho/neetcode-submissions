import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda x:x.start)
        ans = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start >= ans[0]:
                heapq.heappop(ans)
            heapq.heappush(ans, intervals[i].end)
        return len(ans)