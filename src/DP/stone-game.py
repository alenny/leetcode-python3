class Solution:
    def stoneGame(self, piles) -> bool:
        N = len(piles)
        dp = [[piles[i], 0] for i in range(N)]
        for dist in range(1, N):
            for r in range(N - dist):
                c = r + dist
                dp[r][0] = max(piles[r] + dp[r + 1][1], piles[c] + dp[r][1])
                dp[r][1] = piles[r] + sum(dp[r + 1]) - dp[r][0]
        return dp[0][0] > dp[0][1]

    def stoneGame2D(self, piles) -> bool:
        N = len(piles)
        dp = [[[0, 0] for c in range(N)] for r in range(N)]
        for i in range(N):
            dp[i][i] = [piles[i], 0]
        for dist in range(1, N):
            for r in range(N - dist):
                c = r + dist
                dp[r][c][0] = max(piles[r] + dp[r + 1][c][1],
                                  piles[c] + dp[r][c - 1][1])
                dp[r][c][1] = piles[r] + sum(dp[r + 1][c]) - dp[r][c][0]
        return dp[0][N - 1][0] > dp[0][N - 1][1]
