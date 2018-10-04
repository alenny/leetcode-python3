import math


class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = self.findPoint(grid)
        return self.bfs(grid, r, c)

    def bfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        q = [(r, c)]
        visited.add(self.key(r, c))
        dist = 0
        length = 0
        while len(q) > 0:
            nq = []
            for cr, cc in q:
                if grid[cr][cc] == 1:
                    dist += length
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        k = self.key(nr, nc)
                        if not k in visited:
                            nq.append((nr, nc))
                            visited.add(k)
            q = nq
            length += 1
        return dist

    def key(self, r, c):
        return '{0},{1}'.format(r, c)

    def findPoint(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        countsByRow = [0 for r in range(rows)]
        countsByCol = [0 for c in range(cols)]
        totalOnes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    countsByRow[r] += 1
                    countsByCol[c] += 1
                    totalOnes += 1
        prevSum, targetRow = countsByRow[0], 0
        for r in range(1, rows):
            if prevSum - (totalOnes - prevSum) >= 0:
                break
            targetRow = r
            prevSum += countsByRow[r]
        prevSum, targetCol = countsByCol[0], 0
        for c in range(1, cols):
            if prevSum - (totalOnes - prevSum) >= 0:
                break
            targetCol = c
            prevSum += countsByCol[c]
        return targetRow, targetCol


sol = Solution()
# ret = sol.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
ret = sol.minTotalDistance([[0,0,0,1,1,0,0],[0,1,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,0,0,1,0,0],[1,0,0,0,1,1,0],[0,0,1,1,0,0,0],[0,1,0,1,0,0,1],[0,0,1,0,1,1,0],[0,0,0,1,1,1,1]])
print(ret)
