class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        for i1 in range(1, N1 + 1):
            for i2 in range(1, N2 + 1):
                dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1 if text2[i2 - 1] == text1[i1 - 1] \
                    else max(dp[i1 - 1][i2], dp[i1][i2 - 1])
        return dp[N1][N2]


sol = Solution()
ret = sol.longestCommonSubsequence('abcde', 'ace')  # 3
ret = sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy")  # 2
print(ret)
