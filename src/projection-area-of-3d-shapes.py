class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalArea = 0
        highestEachRow = []
        highestEachCol = []
        rows = len(grid)
        cols = len(grid[0])
        for col in range(cols):
            highestEachCol.append(0)
        for row in range(rows):
            highestEachRow.append(0)
            for col in range(cols):
                height = grid[row][col]
                if height == 0:
                    continue
                totalArea += 1
                highestEachRow[row] = max(highestEachRow[row], height)
                highestEachCol[col] = max(highestEachCol[col], height)
        for h in highestEachRow:
            totalArea += h
        for h in highestEachCol:
            totalArea += h
        return totalArea


grid = [[1, 2], [3, 4]]
sol = Solution()
totalArea = sol.projectionArea(grid)
print(totalArea)
