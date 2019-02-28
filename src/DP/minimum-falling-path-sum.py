class Solution:
    def minFallingPathSum(self, A) -> int:
        R, C = len(A), len(A[0])
        dp0 = [A[0][col] for col in range(C)]
        dp1 = [0] * C
        for row in range(1, R):
            if C == 1:
                dp1[0] = dp0[0] + A[row][0]
                continue
            dp1[0] = min(dp0[0], dp0[1]) + A[row][0]
            for col in range(1, C - 1):
                dp1[col] = min(dp0[col - 1], dp0[col],
                               dp0[col + 1]) + A[row][col]
            dp1[C - 1] = min(dp0[C - 2], dp0[C - 1]) + A[row][C - 1]
            dp0, dp1 = dp1, dp0
        return min(dp0)


sol = Solution()
ret = sol.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ret)
