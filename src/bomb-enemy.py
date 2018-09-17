class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maximum = 0
        for r in range(rows):
            enemyInRow = 0
            slots = []
            for c in range(cols):
                if grid[r][c] == '0':
                    grid[r][c] = 0
                    slots.append(c)
                elif grid[r][c] == 'E':
                    enemyInRow += 1
                elif grid[r][c] == 'W':
                    for sc in slots:
                        grid[r][sc] += enemyInRow
                        maximum = max(maximum, grid[r][sc])
                    slots = []
                    enemyInRow = 0
                else:
                    slots.append(c)
            if len(slots) > 0:
                for sc in slots:
                    grid[r][sc] += enemyInRow
                    maximum = max(maximum, grid[r][sc])
        for c in range(cols):
            enemyInCol = 0
            slots = []
            for r in range(rows):
                if grid[r][c] == '0':
                    grid[r][c] = 0
                    slots.append(r)
                elif grid[r][c] == 'E':
                    enemyInCol += 1
                elif grid[r][c] == 'W':
                    for sr in slots:
                        grid[sr][c] += enemyInCol
                        maximum = max(maximum, grid[sr][c])
                    slots = []
                    enemyInCol = 0
                else:
                    slots.append(r)
            if len(slots) > 0:
                for sr in slots:
                    grid[sr][c] += enemyInCol
                    maximum = max(maximum, grid[sr][c])
        return maximum


sol = Solution()
ret = sol.maxKilledEnemies([["W"], ["E"], ["W"], ["0"], ["E"]])
# ret = sol.maxKilledEnemies(
#    [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]])
print('ok')
