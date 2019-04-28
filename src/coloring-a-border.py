class Solution:
    def colorBorder(self, grid, r0: int, c0: int, color: int):
        R, C = len(grid), len(grid[0])
        q = [(r0, c0)]
        color0 = grid[r0][c0]
        borders = set()
        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set((r0, c0))
        while q:
            nq = []
            for r, c in q:
                for dr, dc in deltas:
                    r1, c1 = r + dr, c + dc
                    if r1 < 0 or r1 >= R or c1 < 0 or c1 >= C or grid[r1][c1] != color0:
                        borders.add((r, c))
                        continue
                    if (r1, c1) in visited:
                        continue
                    visited.add((r1, c1))
                    nq.append((r1, c1))
            q = nq
        for r, c in borders:
            grid[r][c] = color
        return grid


sol = Solution()
ret = sol.colorBorder([[1, 2, 2], [2, 3, 2]], 0, 1, 3)
print(ret)
ret = sol.colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]],  1,  1,  2)
print(ret)
