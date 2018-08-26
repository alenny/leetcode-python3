class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for ni in range(n + 1)] for ki in range(k + 1)]
        for ki in range(1, k + 1):
            if n >= 1:
                dp[ki][1] = ki
            if n >= 2:
                dp[ki][2] = ki * ki
            for ni in range(3, n + 1):
                dp[ki][ni] = dp[ki][ni - 1] * (ki - 1) + \
                    dp[ki][ni - 2] * (ki - 1)
        return dp[k][n]


sol = Solution()
ret = sol.numWays(3, 2)
ret = sol.numWays(3, 3)
print(ret)
