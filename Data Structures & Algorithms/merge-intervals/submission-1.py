class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        n = len(intervals)
        i = 1
        ans.append(intervals[0])
        while i < n:
            start1, end1 = ans[-1]
            start2, end2 = intervals[i]

            if start2 <= end1:
                new_start = min(start1, start2)
                new_end = max(end1, end2)
                ans[-1] = [new_start, new_end]
            else:
                ans.append([start2, end2])
            i += 1
        return ans