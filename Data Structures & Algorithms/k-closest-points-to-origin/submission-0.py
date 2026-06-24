class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x, y in points:
            # use negative distance to use max-heap
            dist = -((x ** 2) + (y ** 2))
            heapq.heappush(distance, [dist, x, y])

            if len(distance) > k:
                heapq.heappop(distance)
            
        return [[x, y] for dist, x, y in distance]