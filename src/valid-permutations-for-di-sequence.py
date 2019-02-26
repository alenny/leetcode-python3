class Solution:
    def numPermsDISequence(self, S: str) -> int:
        N = len(S) + 1
        # dp[r][c] means the amount of permutations which satisfy S[:r] and end with number c
        # so for each r, the valid c is in range(0,r+1)
        dp = [[0] * N for r in range(N)]
        dp[0][0] = 1
        for r in range(1, N):
            ch = S[r - 1]
            for c in range(r + 1):
                dp[r][c] = sum(dp[r - 1][c:r]) if ch == 'D' \
                    else sum(dp[r - 1][:c])
        return sum(dp[N - 1]) % (10**9 + 7)


sol = Solution()
ret = sol.numPermsDISequence('DID')
print(ret)
