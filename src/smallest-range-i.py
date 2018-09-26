import math


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        low = math.inf
        high = -math.inf
        for n in A:
            low = min(low, n)
            high = max(high, n)
        return max(0, high - low - 2 * K)
