class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        modFactor = pow(10, 9) + 7
        dp = [0, 0, 1]
        for i in range(3, n + 1):
            dp.append((i - 1) * (dp[i - 2] + dp[i - 1]) % modFactor)
        return dp[n]
