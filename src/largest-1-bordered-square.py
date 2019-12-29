from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        def isSquareOne(row, col, sqrLen):
            bottomRow = row + sqrLen - 1
            rightCol = col + sqrLen - 1
            for r in range(row, row + sqrLen):
                if grid[r][col] != 1 or grid[r][rightCol] != 1:
                    return False
            for c in range(col, col + sqrLen):
                if grid[bottomRow][c] != 1:
                    return False
            return True

        rows, cols = len(grid), len(grid[0])
        maxSL = 0
        for r in range(rows):
            if maxSL >= rows - r:
                break
            for c in range(cols):
                if maxSL >= cols - c:
                    break
                if grid[r][c] != 1:
                    continue
                sc = c + 1
                while sc < cols and grid[r][sc] == 1:
                    sc += 1
                sqrLen = min(sc - c, rows - r)
                while sqrLen > maxSL:
                    if isSquareOne(r, c, sqrLen):
                        maxSL = sqrLen
                        break
                    sqrLen -= 1
        return maxSL * maxSL
