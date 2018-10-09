import itertools


class Solution:
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for r in range(rows)] 
        distinct = 0
        shapeMap = dict()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or visited[r][c]:
                    continue
                shape = self.bfsFindIsland(grid, visited, r, c)
                shapeKey = self.getShapeKey(shape)
                if shapeKey in shapeMap:
                    continue
                # add all possible equivalent shapes to shapeMap
                shapes = [shape, self.getUpDownFlip(shape)]
                for i in range(2):
                    shapes.append(self.getRotate90(shapes[i]))
                    shapes.append(self.getRotate90(shapes[-1]))  # 180
                    shapes.append(self.getRotate90(shapes[-1]))  # 270
                for sp in shapes:
                    sk = self.getShapeKey(sp)
                    shapeMap[sk] = distinct
                distinct += 1
        return distinct

    def bfsFindIsland(self, grid, visited, r, c):
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        visited[r][c] = True
        q = [(r, c)]
        points = [(r, c)]
        minR, maxR, minC, maxC = r, r, c, c
        while len(q) > 0:
            nq = []
            for r0, c0 in q:
                for dr, dc in delta:
                    r1, c1 = r0 + dr, c0 + dc
                    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or visited[r1][c1] or grid[r1][c1] == 0:
                        continue
                    visited[r1][c1] = True
                    nq.append((r1, c1))
                    maxR = max(maxR, r1)
                    minC = min(minC, c1)
                    maxC = max(maxC, c1)
            points.extend(nq)
            q = nq
        islandRows = maxR - minR + 1
        islandCols = maxC - minC + 1
        ret = [['0'] * islandCols for rx in range(islandRows)] 
        for rx, cx in points:
            ret[rx - minR][cx - minC] = '1'
        return ret

    def getShapeKey(self, shape):
        return '{0},{1}|'.format(len(shape), len(shape[0])) + \
            ''.join(itertools.chain.from_iterable(shape))

    def getUpDownFlip(self, shape):
        return [[shape[r][c] for c in range(len(shape[0]))] for r in range(len(shape) - 1, -1, -1)]

    def getRotate90(self, shape):
        return [[shape[r][c] for r in range(len(shape) - 1, -1, -1)] for c in range(len(shape[0]))]

sol = Solution()
ret = sol.numDistinctIslands2([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]])