from collections import defaultdict
import math


class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        yMap = defaultdict(set)
        for x, y in points:
            yMap[y].add(x)
        axis = math.nan
        for y, xSet in yMap.items():
            xList = list(xSet)
            xList.sort()
            centerX = (xList[0] + xList[-1]) / 2
            if not math.isnan(axis) and axis != centerX:
                return False
            for i in range(1, (len(xList) + 1 >> 1)):
                if (xList[i] + xList[len(xList) - 1 - i]) / 2 != centerX:
                    return False
            axis = centerX
        return True


sol = Solution()
ret = sol.isReflected([[-16, 1], [16, 1], [16, 1]])
print(ret)
