class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        houses = len(costs)
        if houses == 0:
            return 0
        dp = [[float('inf') for c in range(3)] for h in range(houses)]
        dp[0] = costs[0][:]
        for h in range(1, houses):
            dp[h][0] = min(dp[h - 1][1], dp[h - 1][2]) + costs[h][0]
            dp[h][1] = min(dp[h - 1][0], dp[h - 1][2]) + costs[h][1]
            dp[h][2] = min(dp[h - 1][1], dp[h - 1][0]) + costs[h][2]
        return min(dp[houses - 1])
