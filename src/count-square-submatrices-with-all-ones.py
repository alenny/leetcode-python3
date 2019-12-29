class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dpSize = [[0] * (C + 1) for r in range(R + 1)]
        dpVOnes = [[0] * (C + 1) for r in range(R + 1)]
        dpHOnes = [[0] * (C + 1) for r in range(R + 1)]
        total = 0
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if matrix[r - 1][c - 1] == 0:
                    dpSize[r][c] = dpHOnes[r][c] = dpVOnes[r][c] = 0
                    continue
                dpVOnes[r][c] = dpVOnes[r - 1][c] + 1
                dpHOnes[r][c] = dpHOnes[r][c - 1] + 1
                dpSize[r][c] = min(dpSize[r - 1][c - 1] + 1, dpVOnes[r][c], dpHOnes[r][c])
                total += dpSize[r][c]
        return total