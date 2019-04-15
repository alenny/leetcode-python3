import math


class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False, False]
        for n in range(2, N + 1):
            ret = False
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0 and not dp[n - i]:
                    ret = True
                    break
            dp.append(ret)
        return dp[-1]


sol = Solution()
ret = sol.divisorGame(1)
print(ret)
ret = sol.divisorGame(2)
print(ret)
ret = sol.divisorGame(3)
print(ret)
ret = sol.divisorGame(4)
print(ret)
