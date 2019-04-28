class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        AL = len(A)
        BL = len(B)
        dp = [[0] * BL for r in range(AL)]
        dp[0][0] = 1 if A[0] == B[0] else 0
        for i in range(1, BL):
            dp[0][i] = max(dp[0][i - 1], 1 if A[0] == B[i] else 0)
        for r in range(1, AL):
            dp[r][0] = max(dp[r - 1][0], 1 if A[r] == B[0] else 0)
            for c in range(1, BL):
                maxLines = max(dp[r][c - 1], dp[r - 1][c])
                if A[r] == B[c]:
                    maxLines = max(maxLines, dp[r - 1][c - 1] + 1)
                dp[r][c] = maxLines
        return dp[AL - 1][BL - 1]


sol = Solution()
ret = sol.maxUncrossedLines([1, 4, 2], [1, 2, 4])
print(ret)
ret = sol.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
print(ret)
ret = sol.maxUncrossedLines([1, 3, 7, 1, 7, 5],  [1, 9, 2, 5, 1])
print(ret)
