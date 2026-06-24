class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # always put in left
        heapq.heappush(self.left, -num)
        # move max(left) into right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # keep size ~=, left holds extra int if odd len
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # odd len, the median is on the left
        if len(self.left) > len(self.right):
            return -self.left[0]
        # even len,
        return (-self.left[0] + self.right[0]) / 2