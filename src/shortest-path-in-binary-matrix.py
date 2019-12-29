class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        N = len(grid)
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        curStep = 1
        points = [(0, 0)]
        visited = set(points)
        while len(points) > 0:
            nextPoints = []
            for x, y in points:
                if x == N - 1 and y == N - 1:
                    return curStep
                for dx, dy in deltas:
                    x1, y1 = x + dx, y + dy
                    if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N or (x1, y1) in visited or grid[x1][y1] == 1:
                        continue
                    nextPoints.append((x1, y1))
                    visited.add((x1, y1))
            points = nextPoints
            curStep += 1
        return -1