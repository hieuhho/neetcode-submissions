class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)

        i = 0
        # add all intervals before newInterval to ans
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # merge overlapping intervals with newIntervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # add the merged newIntervals to ans | add rest of intervals after newIntervals
        ans.append(newInterval)
        ans.extend(intervals[i:])
        return ans