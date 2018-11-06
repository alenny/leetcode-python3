import math


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        cols = len(A[0])
        dp = A[0][:]
        for r in range(1, rows):
            ndp = []
            for c in range(cols):
                ndp.append(min(dp[c - 1] if c > 0 else math.inf, dp[c],
                               dp[c + 1] if c < cols - 1 else math.inf) + A[r][c])
            dp = ndp
        return min(dp)
