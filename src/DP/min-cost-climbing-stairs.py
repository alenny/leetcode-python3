class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        N = len(cost)
        dp = [0] * (N + 1)
        for i in range(2, N + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[N]
