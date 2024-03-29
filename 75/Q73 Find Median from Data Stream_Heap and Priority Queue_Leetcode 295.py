import heapq


class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # uneven size ?
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(8)
print(obj.findMedian())
