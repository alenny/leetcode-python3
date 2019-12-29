import math
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)
        dpSum = [[] for cnt in range(N + 1)]
        dpSum[1] = [0] * N
        dpMax = [[] for cnt in range(N + 1)]
        dpMax[1] = arr[::]
        for cnt in range(2, N + 1):
            dpSum[cnt] = [math.inf] * (N - cnt + 1)
            dpMax[cnt] = [math.inf] * (N - cnt + 1)
            for l in range(N - cnt + 1):
                for r in range(l + 1, l + cnt):
                    val = dpSum[r - l][l] + dpSum[cnt - r + l][r] + dpMax[r - l][l] * dpMax[cnt - r + l][r]
                    dpSum[cnt][l] = min(dpSum[cnt][l], val)
                    dpMax[cnt][l] = max(dpMax[r - l][l], dpMax[cnt - r + l][r])
        return min(dpSum[N])

sol = Solution()
ret = sol.mctFromLeafValues([6,2,4])
print(ret)