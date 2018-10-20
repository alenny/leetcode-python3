import math


class HpInfo:
    def __init__(self, minHp, curHp):
        self.minHp = minHp
        self.curHp = curHp


class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # Best way: from bottom-right to top-left because the result
        # is initial HP which is for the top-left cell
        # dp[r][c] means min HP required to enter cell (r, c) lively
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [math.inf] * cols
        dp[-1] = 1 if dungeon[-1][-1] >= 0 else 1 - dungeon[-1][-1]
        for c in range(cols - 2, -1, -1):
            dp[c] = max(1, dp[c + 1] - dungeon[-1][c])
        for r in range(rows - 2, -1, -1):
            dp[-1] = max(1, dp[-1] - dungeon[r][-1])
            for c in range(cols - 2, -1, -1):
                down = max(1, dp[c] - dungeon[r][c])
                right = max(1, dp[c + 1] - dungeon[r][c])
                dp[c] = min(down, right)
        return dp[0]

    def calculateMinimumHP1D(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # from top-left to bottom-right
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [None for c in range(cols)]
        dp[0] = [HpInfo(dungeon[0][0], dungeon[0][0])]
        for c in range(1, cols):
            curHp = dp[c - 1][0].curHp + dungeon[0][c]
            dp[c] = [HpInfo(min(dp[c - 1][0].minHp, curHp), curHp)]
        for r in range(1, rows):
            curHp = dp[0][0].curHp + dungeon[r][0]
            dp[0] = [HpInfo(min(dp[0][0].minHp, curHp), curHp)]
            for c in range(1, cols):
                dp[c] = self.getCandidates(
                    dp[c], dp[c - 1], dungeon[r][c])
        maxMinHp = -math.inf
        for hpInfo in dp[cols - 1]:
            if hpInfo.minHp > maxMinHp:
                maxMinHp = hpInfo.minHp
        return 1 if maxMinHp >= 0 else 1 - maxMinHp

    def calculateMinimumHP2D(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[None for c in range(cols)] for r in range(rows)]
        dp[0][0] = [HpInfo(dungeon[0][0], dungeon[0][0])]
        for c in range(1, cols):
            curHp = dp[0][c - 1][0].curHp + dungeon[0][c]
            dp[0][c] = [HpInfo(min(dp[0][c - 1][0].minHp, curHp), curHp)]
        for r in range(1, rows):
            curHp = dp[r - 1][0][0].curHp + dungeon[r][0]
            dp[r][0] = [HpInfo(min(dp[r - 1][0][0].minHp, curHp), curHp)]
            for c in range(1, cols):
                dp[r][c] = self.getCandidates(
                    dp[r - 1][c], dp[r][c - 1], dungeon[r][c])
        maxMinHp = -math.inf
        for hpInfo in dp[rows - 1][cols - 1]:
            if hpInfo.minHp > maxMinHp:
                maxMinHp = hpInfo.minHp
        return 1 if maxMinHp >= 0 else 1 - maxMinHp

    def getCandidates(self, dp0, dp1, hpVal):
        candidates = dp0 + dp1
        candidates.sort(key=lambda c: (c.minHp, c.curHp), reverse=True)
        ref = candidates[0]
        curHp = ref.curHp + hpVal
        newCandidates = [HpInfo(min(ref.minHp, curHp), curHp)]
        for i in range(1, len(candidates)):
            if candidates[i].minHp == ref.minHp or candidates[i].curHp <= ref.curHp:
                continue
            curHp = candidates[i].curHp + hpVal
            newCandidates.append(
                HpInfo(min(candidates[i].minHp, curHp), curHp))
            ref = candidates[i]
        return newCandidates


sol = Solution()
ret = sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(ret)
