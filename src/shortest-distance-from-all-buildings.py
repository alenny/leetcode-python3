import math


class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS from building
        totalBuildings = 0
        rows = len(grid)
        cols = len(grid[0])
        # total distances from a 0-cell [r][c] to all reachable buildings
        totalDistances = [[0] * cols for r in range(rows)]
        # total reachable buildings from a 0-cell [r][c]
        totalReached = [[0] * cols for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                totalBuildings += 1
                self.bfsBuilding(grid, r, c, totalDistances, totalReached)
        shortest = math.inf
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and totalReached[r][c] == totalBuildings:
                    shortest = min(shortest, totalDistances[r][c])
        return -1 if shortest == math.inf else shortest

    def bfsBuilding(self, grid, br, bc, totalDistances, totalReached):
        rows = len(grid)
        cols = len(grid[0])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for r in range(rows)]
        q = [(br, bc)]
        visited[br][bc] = True
        dist = 1
        while len(q) > 0:
            nq = []
            for r0, c0 in q:
                for dr, dc in delta:
                    r1, c1 = r0 + dr, c0 + dc
                    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or grid[r1][c1] != 0 or visited[r1][c1]:
                        continue
                    totalDistances[r1][c1] += dist
                    totalReached[r1][c1] += 1
                    visited[r1][c1] = True
                    nq.append((r1, c1))
            q = nq
            dist += 1

    def shortestDistanceFromZero(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalBuildings = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    totalBuildings += 1
        shortest = math.inf
        visited = [[False] * cols for r in range(rows)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 or visited[r][c]:
                    continue
                shortest = min(shortest, self.findPaths(
                    totalBuildings, grid, visited, r, c))
        return shortest if shortest != math.inf else -1

    def findPaths(self, totalBuildings, grid, visited, startR, startC):
        rows = len(grid)
        cols = len(grid[0])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for r in range(rows)]
        q = [(startR, startC)]
        visited[startR][startC] = True
        dist = 0
        totalDist = 0
        while len(q) > 0 and totalBuildings > 0:
            nq = []
            for r, c in q:
                if grid[r][c] == 1:
                    totalDist += dist
                    totalBuildings -= 1
                    continue
                for dr, dc in delta:
                    rx, cx = r + dr, c + dc
                    if rx < 0 or rx >= rows or cx < 0 or cx >= cols or visited[rx][cx] or grid[rx][cx] == 2:
                        continue
                    visited[rx][cx] = True
                    nq.append((rx, cx))
            q = nq
            dist += 1
        return totalDist if totalBuildings == 0 else math.inf
