from collections import defaultdict


class Solution:
    def countCornerRectangles(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 1 or cols == 1:
            return 0
        rowDict = defaultdict(set)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowDict[r].add(c)
        total = 0
        colSets = list(rowDict.values())
        for i, colSet0 in enumerate(colSets):
            for j in range(i + 1, len(colSets)):
                colSet1 = colSets[j]
                sec = colSet0.intersection(colSet1)
                l = len(sec)
                total += l * (l - 1) / 2
        return int(total)

    def countCornerRectanglesBrutal(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 1 or cols == 1:
            return 0
        rowDict = defaultdict(list)
        colDict = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowDict[r].append(c)
                    colDict[c].append(r)
        total = 0
        for c, rowsInCol in colDict.items():
            for i0, r0 in enumerate(rowsInCol):
                colsInRow0 = rowDict[r0]
                j0Begin = 0
                while j0Begin < len(colsInRow0) and colsInRow0[j0Begin] <= c:
                    j0Begin += 1
                if j0Begin == len(colsInRow0):
                    continue
                for i1 in range(i0 + 1, len(rowsInCol)):
                    r1 = rowsInCol[i1]
                    colsInRow1 = rowDict[r1]
                    j0, j1 = j0Begin, 0
                    while j1 < len(colsInRow1) and colsInRow1[j1] <= c:
                        j1 += 1
                    while j0 < len(colsInRow0) and j1 < len(colsInRow1):
                        if colsInRow0[j0] > colsInRow1[j1]:
                            j1 += 1
                        elif colsInRow0[j0] < colsInRow1[j1]:
                            j0 += 1
                        else:
                            total += 1
                            j1 += 1
                            j0 += 1
        return total
