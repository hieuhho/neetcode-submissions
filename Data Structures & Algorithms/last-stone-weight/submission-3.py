class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        myHeap = stones
        heapq.heapify_max(myHeap)

        while len(myHeap) > 1:
            x = heapq.heappop_max(myHeap)
            y = heapq.heappop_max(myHeap)
            if x == y:
                continue
            if y < x:
                heapq.heappush_max(myHeap, x - y)

        return 0 if not myHeap else myHeap[0]