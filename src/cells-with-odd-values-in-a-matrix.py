class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rowInc = [0] * n
        colInc = [0] * m
        for ri, ci in indices:
            rowInc[ri] += 1
            colInc[ci] += 1
        ret = 0
        for r in range(n):
            for c in range(m):
                if (rowInc[r] + colInc[c]) % 2 == 1:
                    ret += 1
        return ret