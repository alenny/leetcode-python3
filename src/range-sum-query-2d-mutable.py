from collections import defaultdict


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])
        if cols == 0:
            return
        self.matrix = matrix
        self.sums = [[0] * cols for r in range(rows)]
        total = 0
        for c in range(cols):
            total += matrix[0][c]
            self.sums[0][c] = total
        for r in range(1, rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                self.sums[r][c] = total + self.sums[r - 1][c]
        self.changes = defaultdict(dict)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.changes[row][col] = val - self.matrix[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        delta = 0
        for r, cs in self.changes.items():
            if r < row1 or r > row2:
                continue
            for c, change in cs.items():
                if c >= col1 and c <= col2:
                    delta += change
        if row1 > 0 and col1 > 0:
            return self.sums[row2][col2] - self.sums[row2][col1 - 1] \
                - self.sums[row1 - 1][col2] + self.sums[row1 - 1][col1 - 1] \
                + delta
        if row1 > 0:
            return self.sums[row2][col2] - self.sums[row1 - 1][col2] + delta
        if col1 > 0:
            return self.sums[row2][col2] - self.sums[row2][col1 - 1] + delta
        # rows == 0 and cols == 0:
        return self.sums[row2][col2] + delta


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[2, 4], [-3, 5]])
obj.update(0, 1, 3)
obj.update(1, 1, -3)
obj.update(0, 1, 1)
ret = obj.sumRegion(0, 0, 1, 1)
