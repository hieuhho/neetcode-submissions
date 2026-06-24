class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])

        ans = {}
        heap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                interval = end - start + 1
                heapq.heappush(heap, [interval, end])
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            ans[q] = heap[0][0] if heap else -1
        return [ans[q] for q in queries]