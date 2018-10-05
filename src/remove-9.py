import math


class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = int(math.log10(n))
        dp = [0]
        for i in range(1, m + 2):
            dp.append(9 * dp[i - 1] + 10**(i - 1))
        total9 = self.findTotal9(n, dp)
        return n + total9

    def findTotal9(self, n, dp):
        if n < 9:
            return 0
        prevTotal9 = -1
        total9 = 0
        num = n
        while total9 > prevTotal9:
            prevTotal9 = total9
            total9 = 0
            while num > 0:
                x = int(math.log10(num))
                x10 = 10**x
                y = int(num / x10)
                total9 += y * dp[x]
                if y == 9:
                    total9 += x10
                    break
                num %= y * x10
            num = n + total9
        return total9


sol = Solution()
ret = sol.newInteger(9)
ret = sol.newInteger(10)
ret = sol.newInteger(18)
ret = sol.newInteger(1000)
ret = sol.newInteger(100000)
print(ret)
