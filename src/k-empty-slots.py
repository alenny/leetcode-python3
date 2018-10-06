class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        # first convert to an array indexed by position
        days = [-1] * n
        for day, pos in enumerate(flowers, 1):
            days[pos - 1] = day
        firstDay = n + 1
        left = 0
        while left < n - k - 1:
            right = left + k + 1
            x = max(days[left], days[right])
            minDayPos, minDay = min(
                enumerate(days[left + 1:right], left + 1), key=lambda pair: pair[1]) \
                if k > 0 else (-1, n + 1)
            if minDay > x:
                firstDay = min(firstDay, x)
                left = right
            else:
                left = minDayPos
        return -1 if firstDay == n + 1 else firstDay


sol = Solution()
ret = sol.kEmptySlots([3, 9, 2, 8, 1, 6, 10, 5, 4, 7], 1)
print(ret)
