class Solution:
    def numEnclaves(self, A) -> int:
        N1 = 0
        rows, cols = len(A), len(A[0])
        q = []
        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 0:
                    continue
                N1 += 1
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    q.append((r, c))
        visitedOnes = set(q)
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            nq = []
            for r, c in q:
                for dr, dc in deltas:
                    r1, c1 = r + dr, c + dc
                    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or A[r1][c1] == 0 or (r1, c1) in visitedOnes:
                        continue
                    visitedOnes.add((r1, c1))
                    nq.append((r1, c1))
            q = nq
        return N1 - len(visitedOnes)


sol = Solution()
# ret = sol.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
ret = sol.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])
print(ret)
