class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        modulo = 10**9 + 7
        # sources = [[4, 6], [6, 8], [7, 9], [4, 8],
        #            [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        # keys = [0, 1, 2, 4, 5, 7, 8]
        sources = [[3, 3], [3, 6], [5, 5], [0, 1, 5], [], [2, 3], [1, 1]]
        K = len(sources)
        dp = [1] * K
        while N > 1:
            nextDp = [0] * K
            for ki in range(K):
                for si in sources[ki]:
                    nextDp[ki] = (nextDp[ki] + dp[si]) % modulo
            dp = nextDp
            N -= 1
        return (sum(dp) + dp[1] + dp[3] + dp[5]) % modulo


sol = Solution()
ret = sol.knightDialer(1)
ret = sol.knightDialer(2)
ret = sol.knightDialer(3)
ret = sol.knightDialer(4)
ret = sol.knightDialer(161)
print(ret)
