from collections import defaultdict
import math


class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        N = len(points)
        relations = [defaultdict(set) for i in range(N)]
        ijMap = dict()
        for i, (x0, y0) in enumerate(points):
            for j, (x1, y1) in enumerate(points[i + 1:], i + 1):
                incline = self.getIncline(x0, y0, x1, y1)
                relations[i][incline].add(j)
                relations[j][incline].add(i)
                ijMap[(i, j)] = ijMap[(j, i)] = incline
        minArea = math.inf
        for i0 in range(N):
            for i1 in range(i0 + 1, N):
                inc01 = ijMap[(i0, i1)]
                inc02 = self.getRevIncline(*inc01)
                i3Set = relations[i1][inc02]
                for i2 in relations[i0][inc02]:
                    if not i3Set.isdisjoint(relations[i2][inc01]):
                        minArea = min(
                            minArea, self.calArea(points, i0, i1, i2))
        return minArea if minArea != math.inf else 0

    def calArea(self, points, i0, i1, i2):
        x0, y0 = points[i0]
        x1, y1 = points[i1]
        x2, y2 = points[i2]
        return math.sqrt(((x1 - x0)*(x1 - x0) + (y1 - y0) * (y1 - y0)) * ((x2 - x0) * (x2 - x0) + (y2 - y0) * (y2 - y0)))

    def getRevIncline(self, dy, dx):
        if dy == math.inf:
            return 0, 1
        if dy == 0:
            return math.inf, 1
        return (-dx, dy) if dy > 0 else (dx, -dy)

    def getIncline(self, x0, y0, x1, y1):
        if x0 == x1:
            return math.inf, 1
        if y0 == y1:
            return 0, 1
        dx, dy = x1 - x0, y1 - y0
        cf = self.getCommonFactor(dx, dy)
        dx, dy = dx // cf, dy // cf
        return (dy, dx) if dx > 0 else (-dy, -dx)

    def getCommonFactor(self, a, b):
        a, b = abs(a), abs(b)
        a = a % b
        while a != 0:
            b = b % a
            a, b = b, a
        return b


sol = Solution()
# ret = sol.minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]])
ret = sol.minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]])
print(ret)
