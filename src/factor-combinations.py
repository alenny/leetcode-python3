import math


class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = self.factorHelper(n, 2, dict())
        return ret

    def factorHelper(self, n, mini, cache):
        if n in cache:
            return cache[n]
        factors = []
        for i in range(mini, int(math.sqrt(n)) + 1):
            if n % i != 0:
                continue
            f = int(n / i)
            if f < i:
                break
            factors.append([i, f])
            subRet = self.factorHelper(f, i, cache)
            for r in subRet:
                if r[0] >= i:
                    factors.append([i] + r)
        cache[n] = factors
        return factors


sol = Solution()
ret = sol.getFactors(32)
