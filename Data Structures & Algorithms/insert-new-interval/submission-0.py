class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]

        n = len(intervals)
        for i in range(1, n):
            start1, stop1 = ans[-1]
            start2, stop2 = intervals[i]

            if stop1 >= start2:
                ans[-1] = [start1, max(stop1, stop2)]
            else:
                ans.append(intervals[i])
        return ans