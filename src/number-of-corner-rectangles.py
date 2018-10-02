class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows < 2 or cols < 2:
            return 0
        total = 0
        for r0 in range(rows):
            for r1 in range(r0 + 1, rows):
                colOnePairs = 0
                for c in range(cols):
                    if grid[r0][c] == 1 and grid[r1][c] == 1:
                        colOnePairs += 1
                total += colOnePairs * (colOnePairs - 1) / 2
        return int(total)

    def countCornerRectanglesByPickingOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows < 2 or cols < 2:
            return 0
        inRows = [[] for r in range(rows)]
        inCols = [[] for c in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                inRows[r].append(c)
                inCols[c].append(r)
        total = 0
        for r0 in range(rows - 1):
            for r1 in range(r0 + 1, rows):
                colPairs = self.findSameCols(inRows, r0, r1)
                total += colPairs * (colPairs - 1) / 2
        return int(total)

    def findSameCols(self, inRows, r0, r1):
        c0i, c1i = 0, 0
        sameCount = 0
        while c0i < len(inRows[r0]) and c1i < len(inRows[r1]):
            if inRows[r0][c0i] < inRows[r1][c1i]:
                c0i += 1
            elif inRows[r0][c0i] > inRows[r1][c1i]:
                c1i += 1
            else:
                sameCount += 1
                c0i += 1
                c1i += 1
        return sameCount

    def countCornerRectanglesForce(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows < 2 or cols < 2:
            return 0
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                for c1 in range(c + 1, cols):
                    if grid[r][c1] == 0:
                        continue
                    for r1 in range(r + 1, rows):
                        if grid[r1][c] == 1 and grid[r1][c1] == 1:
                            total += 1
        return total
