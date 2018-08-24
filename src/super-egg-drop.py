class Solution:
    def superEggDropDP(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [0 for n in range(N + 1)]
        for n in range(1, N + 1):
            dp[n] = n
        for k in range(2, K + 1):
            dp1 = [0 for n in range(N + 1)]
            dp1[1] = 1
            for n in range(2, N + 1):
                dp1[n] = n
                for mid in range(2, n):
                    dp1[n] = min(dp1[n], 1 + max(dp[mid - 1], dp1[n - mid]))
            dp = dp1
        return dp[N]

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        cache = []
        for k in range(K+1):
            cache.append(dict())
        ret = self.process(K, N, cache)
        return ret

    def process(self, k, length, cache):
        if k <= 0:
            return 0
        if k == 1 or length <= 1:
            return max(length, 0)
        if length in cache[k]:
            return cache[k][length]
        ret = length
        mid = length + 1 >> 1
        while mid > 0:
            low = self.process(k - 1, mid - 1, cache)
            high = self.process(k, length - mid, cache)
            if (low == high or mid == 1):
                ret = min(ret, 1 + max(low, high))
                break
            mid -= 1
        cache[k][length] = ret
        return ret


sol = Solution()
# ret = sol.superEggDrop(2, 6)
ret = sol.superEggDrop(4, 10000)
print(ret)
