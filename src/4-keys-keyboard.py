class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0, 1, 2, 3, 4, 5]
        for i in range(6, N + 1):
            dp.append(0)
            for v in range(4):
                dp[i] = max(dp[i], dp[i - 3 - v] * (v + 2))
        return dp[N]


sol = Solution()
ret = sol.maxA(6)
print(ret)
