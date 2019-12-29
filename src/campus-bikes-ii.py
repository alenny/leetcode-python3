import math
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        WL = len(workers)
        BL = len(bikes)

        # dp[wi][flag] means the shortest distance for the remaining (WL-wi) users with the remaining bikes marked as 0 in flag bits.
        dp = [{} for wi in range(WL)]

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        def backtrack(cw, flag):
            if cw >= WL:
                return 0
            if flag in dp[cw]:
                return dp[cw][flag]
            shortest = math.inf
            for bi in range(BL):
                if flag & (1 << bi):
                    continue
                remainingShortest = backtrack(cw + 1, flag | (1 << bi))
                shortest = min(shortest, dist(cw, bi) + remainingShortest)
            dp[cw][flag] = shortest
            return shortest

        return backtrack(0, 0)

sol = Solution()
ret = sol.assignBikes([[815,60],[638,626],[6,44],[103,90],[591,880]], [[709,161],[341,339],[755,955],[172,27],[433,489]])
print(ret)