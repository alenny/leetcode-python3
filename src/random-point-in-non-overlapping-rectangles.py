from collections import defaultdict
from random import randint


class Record:
    def __init__(self):
        self.count = 0
        self.ranges = []


class Solution:

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.total = 0
        self.counts = []
        for rect in rects:
            self.total += self.countPointsInRect(*rect)
            self.counts.append(self.total)

    def pick(self):
        """
        :rtype: List[int]
        """
        num = randint(1, self.total)
        targetRect = None
        pos = 0
        for i in range(len(self.counts)):
            if num <= self.counts[i]:
                targetRect = self.rects[i]
                pos = self.counts[i] - num
                break
        x0, y0, x1, y1 = targetRect
        colLen = y1 - y0 + 1
        return [int(pos / colLen) + x0, pos % colLen + y0]

    def countPointsInRect(self, x0, y0, x1, y1):
        return (x1 - x0 + 1) * (y1 - y0 + 1)

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


# sol = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
sol = Solution([[1, 1, 5, 5]])
ret = sol.pick()
print(ret)
