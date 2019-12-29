from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        # dpFirst[i][m] = the most stones the first moved person can get from the last i piles when M == m  
        dpFirst = [[0] * (N + 1) for i in range(N + 1)]
        # dpSecond[i][m] = the most stones the second moved person can get from the last i piles when M == m  
        dpSecond = [[0] * (N + 1) for i in range(N + 1)]

        def dfs(i, m):
            if i == 0:
                return 0, 0
            if dpFirst[i][m] > 0:
                return dpFirst[i][m], dpSecond[i][m]
            totalThisRound = 0
            j = N - i
            while j < N:
                c = j - (N - i) + 1
                if c > 2 * m:
                    break
                totalThisRound += piles[j]
                prevFirst, prevSecond = dfs(i - c, max(m, c))
                finalTotal = prevSecond + totalThisRound
                if (finalTotal > dpFirst[i][m]):
                    dpFirst[i][m] = finalTotal
                    dpSecond[i][m] = prevFirst
                j += 1
            return dpFirst[i][m], dpSecond[i][m]

        return dfs(N, 1)[0]

sol = Solution()
ret = sol.stoneGameII([2,7,9,4,4])
print(ret)