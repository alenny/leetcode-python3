import math


class Solution:
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        xLen = len(image)
        yLen = len(image[0])
        minX = minY = math.inf
        maxX = maxY = -math.inf
        q = [(x, y)]
        visited = [[False for y in range(yLen)] for x in range(xLen)]
        while len(q) > 0:
            nq = []
            for x0, y0 in q:
                minX = min(minX, x0)
                maxX = max(maxX, x0)
                minY = min(minY, y0)
                maxY = max(maxY, y0)
                for dx, dy in deltas:
                    x1, y1 = x0 + dx, y0 + dy
                    if x1 < 0 or x1 >= xLen or y1 < 0 or y1 >= yLen or visited[x1][y1] or image[x1][y1] == '0':
                        continue
                    visited[x1][y1] = True
                    nq.append((x1, y1))
            q = nq
        return (maxX - minX + 1) * (maxY - minY + 1)
