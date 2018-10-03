import math


class Solution:
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1
        factors = []
        f = 9
        while a > 1 and f >= 2:
            if a % f != 0:
                f -= 1
                continue
            factors.append(str(f))
            a = int(a / f)
        if a > 1:
            return 0
        factors.reverse()
        ret = int(''.join(factors))
        return ret if ret < pow(2, 31) else 0

    def smallestFactorizationBackTracking(self, a):
        """
        :type a: int
        :rtype: int
        """
        ret = self.helper(a, [])
        return ret if ret < pow(2, 31) else 0

    def helper(self, a, factors):
        if a < 10:
            return int(''.join(factors)) * 10 + a if len(factors) > 0 else a
        minimum = math.inf
        for i in range(int(factors[-1]) if len(factors) > 0 else 2, int(math.sqrt(a)) + 1):
            if a % i != 0:
                continue
            factors.append(str(i))
            minimum = min(minimum, self.helper(int(a / i), factors))
            factors.pop()
        return minimum


sol = Solution()
ret = sol.smallestFactorization(48)
print(ret)
