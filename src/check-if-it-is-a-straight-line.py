from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]:
            if x1 == x0 and x != x0 or x1 != x0 and y != y0 + (y1 - y0) / (x1 - x0) * (x - x0):
                return False
        return True

sol = Solution()
ret = sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
print(ret)