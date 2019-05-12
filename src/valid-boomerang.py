from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        def getMaxCommonFactor(a, b):
            a = a % b
            while a > 0:
                c = b % a
                b = a
                a = c
            return b

        def getCline(x0, y0, x1, y1):
            dx, dy = x1 - x0, y1 - y0
            if dx == 0 and dy == 0:
                return (0, 0)
            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)
            cf = getMaxCommonFactor(abs(dx), abs(dy))
            return (dx // cf, dy // cf)

        c1 = getCline(points[0][0], points[0][1], points[1][0], points[1][1])
        c2 = getCline(points[0][0], points[0][1], points[2][0], points[2][1])
        c3 = getCline(points[1][0], points[1][1], points[2][0], points[2][1])
        return c1 != (0, 0) and c2 != (0, 0) and c3 != (0, 0) and c1 != c2


sol = Solution()
# ret = sol.isBoomerang([[1, 1], [2, 2], [3, 3]])
ret = sol.isBoomerang([[1, 0], [0, 0], [2, 0]])
print(ret)
