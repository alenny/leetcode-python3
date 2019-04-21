class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [[r0, c0]]
        q = [(r0, c0)]
        visited = set([(r0, c0)])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            nq = []
            for r, c in q:
                for dr, dc in deltas:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    ret.append([nr, nc])
                    nq.append((nr, nc))
            q = nq
        return ret
