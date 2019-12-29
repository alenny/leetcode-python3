from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        N = len(stones)
        li = ri = 0
        maxInWindow = 0
        while ri < N:
            if stones[ri] >= stones[li] + N:
                maxInWindow = max(maxInWindow, ri - li)
                li += 1
            else:
                ri += 1
        minSteps = 2 \
            if maxInWindow == N - 1 and (stones[1] - stones[0] > 1 or stones[-1] - stones[-2] > 1) \
            else N - maxInWindow
        maxStep
