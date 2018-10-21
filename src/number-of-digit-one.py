import math


class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        power = int(math.log10(n))
        dp = self.helper(power)
        totalOnes = 0
        while n > 0:
            powerResult = 10**power
            f = int(n / powerResult)
            n %= powerResult
            if f == 1:
                totalOnes += dp[power] + n + 1
            elif f > 1:
                totalOnes += dp[power] * f + powerResult
            power -= 1
        return totalOnes

    def helper(self, power):
        # count digits one in numbers less than 10**power
        dp = [0, 1]
        for p in range(2, power + 1):
            dp.append(dp[p - 1] * 9 + dp[p - 1] + 10**(p - 1))
        return dp


sol = Solution()
ret = sol.countDigitOne(100)
print(ret)
