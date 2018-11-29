class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [[0] * (L + 1) for n in range(N + 1)]
        dp[1][1] = 1
        if K == 0:
            for l in range(2, L + 1):
                dp[1][l] = 1
        for n in range(2, N + 1):
            for l in range(n, L + 1):
                dp[n][l] = dp[n - 1][l - 1] * n + dp[n][l - 1] * max(0, n - K)
        return dp[N][L] % mod


sol = Solution()
ret = sol.numMusicPlaylists(16, 19, 5)
# ret = sol.numMusicPlaylists(2, 3, 1)
print(ret)
