class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.rows = len(A)
        self.cols = len(A[0])
        edges = set()
        visited = [[False] * self.cols for r in range(self.rows)]
        foundFirst = False
        for r in range(self.rows):
            for c in range(self.cols):
                if A[r][c] == 0:
                    continue
                # found one island, and marked as 2
                self.bfs(A, visited, r, c, edges)
                foundFirst = True
                break
            if foundFirst:
                break
        # bfs edges
        dist = 1
        q = []
        for edge in edges:
            r, c = self.decodePos(edge)
            q.append((r, c))
            visited[r][c] = True
        while len(q) > 0:
            nq = []
            for r0, c0 in q:
                for dr, dc in self.deltas:
                    r1, c1 = r0 + dr, c0 + dc
                    if r1 < 0 or r1 >= self.rows or c1 < 0 or c1 >= self.cols or visited[r1][c1]:
                        continue
                    if A[r1][c1] == 1:
                        return dist
                    nq.append((r1, c1))
                    visited[r1][c1] = True
            q = nq
            dist += 1
        return dist

    def bfs(self, A, visited, r, c, edges):
        q = [(r, c)]
        visited[r][c] = True
        while len(q) > 0:
            nq = []
            for r0, c0 in q:
                A[r0][c0] = 2
                for dr, dc in self.deltas:
                    r1, c1 = r0 + dr, c0 + dc
                    if r1 < 0 or r1 >= self.rows or c1 < 0 or c1 >= self.cols or visited[r1][c1]:
                        continue
                    if A[r1][c1] == 0:
                        edges.add(self.encodePos(r1, c1))
                    else:
                        visited[r1][c1] = True
                        nq.append((r1, c1))
            q = nq

    def encodePos(self, r, c):
        return '{0},{1}'.format(r, c)

    def decodePos(self, txt):
        parts = txt.split(',')
        return int(parts[0]), int(parts[1])


sol = Solution()
ret = sol.shortestBridge([[0, 1], [1, 0]])
# ret = sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
print(ret)
