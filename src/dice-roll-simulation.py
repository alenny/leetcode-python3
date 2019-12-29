from typing import List

class Solution:
    # explanation: https://leetcode.com/problems/dice-roll-simulation/discuss/441800/Very-short-python-solution-faster-than-89.95
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        R = [0] + rollMax
        dpCountOf = [0] * (n + 1)
        dpCountOf[1] = 6
        dpCountEndOfK = [[0] * 7 for r in range(n + 1)]
        for k in range(1, 7):
            dpCountEndOfK[1][k] = 1
        for rolls in range(2, n + 1):
            for k in range(1, 7):
                invalidCount = dpCountOf[rolls - (R[k] + 1)] - dpCountEndOfK[rolls - (R[k] + 1)][k] if R[k] + 1 < rolls else (1 if R[k] + 1 == rolls else 0)
                dpCountEndOfK[rolls][k] = dpCountOf[rolls - 1] - invalidCount
                dpCountOf[rolls] += dpCountEndOfK[rolls][k]
        return dpCountOf[n] % (10**9 + 7)

sol = Solution()
ret = sol.dieSimulator(20, [8,5,10,8,7,2])
print(ret)