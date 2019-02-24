from collections import defaultdict


class Solution:
    def gridIllumination(self, N: int, lamps, queries):
        rowHolders = defaultdict(int)
        colHolders = defaultdict(int)
        diffDiagHolders = defaultdict(int)
        sumDiagHolders = defaultdict(int)
        lampSet = set()
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r, c in lamps:
            lampSet.add((r, c))
            self.addToHolders(r, c, rowHolders, colHolders,
                              diffDiagHolders, sumDiagHolders)
        ret = []
        for r, c in queries:
            ret.append(1 if self.isLighted(
                r, c, rowHolders, colHolders, diffDiagHolders, sumDiagHolders) else 0)
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N or not (nr, nc) in lampSet:
                    continue
                self.removeFromHolders(
                    nr, nc, rowHolders, colHolders, diffDiagHolders, sumDiagHolders)
                lampSet.remove((nr, nc))
        return ret

    def addToHolders(self, r, c, rowHolders, colHolders, diffDiagHolders, sumDiagHolders):
        rowHolders[r] += 1
        colHolders[c] += 1
        diffDiagHolders[r - c] += 1
        sumDiagHolders[r + c] += 1

    def removeFromHolders(self, r, c, rowHolders, colHolders, diffDiagHolders, sumDiagHolders):
        self.removeHelper(r, rowHolders)
        self.removeHelper(c, colHolders)
        self.removeHelper(r - c, diffDiagHolders)
        self.removeHelper(r + c, sumDiagHolders)

    def removeHelper(self, key, holders):
        if key in holders:
            holders[key] -= 1
            if holders[key] == 0:
                holders.pop(key)

    def isLighted(self, r, c, rowHolders, colHolders, diffDiagHolders, sumDiagHolders):
        return r in rowHolders or c in colHolders or (r - c) in diffDiagHolders or (r + c) in sumDiagHolders


sol = Solution()
ret = sol.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]])
print(ret)
