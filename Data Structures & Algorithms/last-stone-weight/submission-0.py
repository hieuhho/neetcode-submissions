class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negatives so we can simulate a max heap using Python’s min heap. heapq is ONLY minheap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            # Pop two smallest (most negative =  two heaviest stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:                              # second stone is smaller
                heapq.heappush(stones, first - second)      # Push the new stone (difference), keeping negatives
        return abs(stones[-1]) if stones else 0