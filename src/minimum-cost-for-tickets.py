class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [0] * (1 + len(days))
        for di, d in enumerate(days):
            dp[di + 1] = dp[di] + costs[0]
            # 7-day ticket to today
            dj = di
            while dj >= 0 and days[dj] > d - 7:
                dj -= 1
            dp[di + 1] = min(dp[di + 1], dp[dj + 1] + costs[1])
            # 30-day ticket to today
            while dj >= 0 and days[dj] > d - 30:
                dj -= 1
            dp[di + 1] = min(dp[di + 1], dp[dj + 1] + costs[2])
        return dp[len(days)]


sol = Solution()
ret = sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
print(ret)
