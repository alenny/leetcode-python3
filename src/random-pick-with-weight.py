from random import randint
import math


class Solution:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sumW = [w[0]]
        total = w[0]
        for i in range(1, len(w)):
            total += w[i]
            self.sumW.append(total)

    def pickIndex(self):
        """
        :rtype: int
        """
        weight = randint(0, self.sumW[-1] - 1)
        return self.binarySearch(weight, 0, len(self.sumW) - 1)

    def binarySearch(self, weight, begin, end):
        while begin < end:
            mid = begin + end >> 1
            if self.sumW[mid] <= weight:
                begin = mid + 1
            else:
                end = mid
        return begin

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
