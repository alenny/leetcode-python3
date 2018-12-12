class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        rods.sort()
        maxHalf = sum(rods) >> 1
        dp = [None for half in range(maxHalf + 1)]
        dp[0] = (0, 0)
        prevMax = 0
        for r in rods:
            if r > maxHalf:
                break
            dp1 = dp[:]
            for j in range(prevMax + 1):
                if dp[j] == None:
                    continue
                if j + r <= maxHalf and (dp1[j + r] == None or dp[j][0] > dp1[j + r][0]):
                    dp1[j + r] = (dp[j][0], dp[j][1] + r)
                if r > j and (dp1[r - j] == None or dp[j][1] > dp1[r - j][0]):
                    dp1[r - j] = (dp[j][1], dp[j][0] + r)
                elif j >= r and (dp1[j - r] == None or dp[j][1] > dp1[j - r][1]):
                    dp1[j - r] = (dp[j][0] + r, dp[j][1])
            dp = dp1
            prevMax = min(prevMax + r, maxHalf)
        return dp[0][0]


sol = Solution()
ret = sol.tallestBillboard([1, 2])
print(ret)
