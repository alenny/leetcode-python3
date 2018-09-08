class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        edgeMap = [[] for i in range(n)]
        for n0, n1 in edges:
            edgeMap[n0].append(n1)
            edgeMap[n1].append(n0)
        visited = [False for i in range(n)]
        q = [(0, -1)]
        visited[0] = True
        totalVisited = 1
        while len(q) > 0:
            nq = []
            for nx, parent in q:
                for nnx in edgeMap[nx]:
                    if nnx == parent:
                        continue
                    if visited[nnx]:
                        return False
                    nq.append((nnx, nx))
                    visited[nnx] = True
                    totalVisited += 1
            q = nq
        return totalVisited == n


sol = Solution()
ret = sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
