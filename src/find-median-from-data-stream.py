import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.total = 0
        self.heap0 = []
        self.heap1 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # use min heap to track the bigger half of the numbers
        # the heap top is close to the median
        self.total += 1
        newHeapLen = (self.total >> 1) + 1
        if len(self.heap0) == newHeapLen:
            if num > self.heap0[0]:
                heapq.heappush(self.heap1, -heapq.heappop(self.heap0))
                heapq.heappush(self.heap0, num)
            else:
                heapq.heappush(self.heap1, -num)
        elif len(self.heap0) == 0 or len(self.heap1) == 0 or num >= -self.heap1[0]:
            heapq.heappush(self.heap0, num)
        else:
            heapq.heappush(self.heap1, -num)
            heapq.heappush(self.heap0, -heapq.heappop(self.heap1))

    def findMedian(self):
        """
        :rtype: float
        """
        if self.total == 0:
            return 0
        if self.total % 2 == 1:
            return self.heap0[0]
        return (self.heap0[0] + self.heap0[1]) / 2 if len(self.heap0) == 2 else (self.heap0[0] + min(self.heap0[1:3])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
ret = mf.findMedian()
mf.addNum(3)
ret = mf.findMedian()
