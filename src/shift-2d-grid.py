from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ret = [[0] * m for r in range(n)]
        for r in range(n):
            for c in range(m):
                r1 = (r + (c + k) // m) % n
                c1 = (c + k) % m
                ret[r1][c1] = grid[r][c]
        return ret