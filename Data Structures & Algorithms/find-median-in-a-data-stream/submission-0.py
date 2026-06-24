class MedianFinder:

    def __init__(self):
        self.left_half = []       # max heap, stores min -> mid | use neg num so [0]
        self.right_half = []       # min heap stores mid -> max | use mid

    def addNum(self, num: int) -> None:
        middle = self.right_half[0] if self.right_half else float("inf")
        if middle < num:
            heapq.heappush(self.right_half, num)
        else:
            heapq.heappush(self.left_half, -num)

        if len(self.left_half) > len(self.right_half)  + 1:
            # "left is longer"
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        elif len(self.right_half) > len(self.left_half)  + 1:
            # "right is longer"
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))


    def findMedian(self) -> float:
        len_diff = len(self.left_half) - len(self.right_half)

        if len(self.left_half) > len(self.right_half):
            return -self.left_half[0]
        if len(self.right_half) > len(self.left_half):
            return self.right_half[0]
        return (-self.left_half[0] + self.right_half[0]) / 2

