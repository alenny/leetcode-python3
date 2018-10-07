import math


class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        modulo = 10**9 + 7
        rectangles.sort(key=lambda rec: rec[0], reverse=True)
        allX = list(set([rec[0] for rec in rectangles] +
                        [rec[2] for rec in rectangles]))
        allX.sort()
        totalArea = 0
        for xi in range(len(allX) - 1):
            xLeft, xRight = allX[xi], allX[xi + 1]
            recToHandle = []
            while len(rectangles) > 0 and rectangles[-1][0] == xLeft:
                recToHandle.append(rectangles.pop())
            recToHandle.sort(key=lambda rec: rec[1])  # sort by y0
            maxY1 = -math.inf
            for x0, y0, x1, y1 in recToHandle:
                totalArea += max(0, (y1 - max(maxY1, y0)) * (xRight - xLeft))
                maxY1 = max(maxY1, y1)
                if x1 > xRight:
                    rectangles.append([xRight, y0, x1, y1])
        return totalArea % modulo


sol = Solution()
ret = sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])
# ret = sol.rectangleArea([[0, 0, 3, 3], [2, 0, 5, 3], [1, 1, 4, 4]])
print(ret)
