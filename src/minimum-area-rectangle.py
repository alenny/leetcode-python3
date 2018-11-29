from collections import defaultdict
import math


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xMap = defaultdict(set)
        for px, py in points:
            xMap[px].add(py)
        minArea = math.inf
        xList = list(xMap.items())
        for i, (x0, ySet0) in enumerate(xList):
            for x1, ySet1 in xList[i + 1:]:
                ySet = ySet0.intersection(ySet1)
                if len(ySet) < 2:
                    continue
                yList = sorted(ySet)
                minDy = math.inf
                for yi in range(1, len(yList)):
                    minDy = min(minDy, yList[yi] - yList[yi - 1])
                minArea = min(minArea, abs(x1 - x0) * minDy)
        return 0 if minArea == math.inf else minArea

    def minAreaRect1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xMap = defaultdict(set)
        yMap = defaultdict(set)
        for px, py in points:
            xMap[px].add(py)
            yMap[py].add(px)
        minArea = math.inf
        for x0, ySet in xMap.items():
            for y0 in ySet:
                for x1 in yMap[y0]:
                    if x1 == x0:
                        continue
                    for y1 in xMap[x1]:
                        if y1 != y0 and y1 in ySet:
                            minArea = min(minArea, abs(y1 - y0)*abs(x1 - x0))
        return minArea if minArea != math.inf else 0


sol = Solution()
ret = sol.minAreaRect([[1, 2], [0, 1], [1, 3], [3, 3], [0, 4], [
                      1, 4], [2, 2], [4, 2], [1, 0], [2, 4], [4, 0]])
