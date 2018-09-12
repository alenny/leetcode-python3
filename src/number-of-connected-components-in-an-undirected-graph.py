from collections import defaultdict


class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edgeMap = defaultdict(list)
        visited = [False for i in range(n)]
        for n0, n1 in edges:
            edgeMap[n0].append(n1)
            edgeMap[n1].append(n0)
        count = 0
        for node in range(n):
            if visited[node]:
                continue
            self.bfs(edgeMap, visited, node)
            count += 1
        return count

    def bfs(self, edgeMap, visited, node):
        q = [node]
        visited[node] = True
        while len(q) > 0:
            nq = []
            for curr in q:
                for nx in edgeMap[curr]:
                    if visited[nx]:
                        continue
                    visited[nx] = True
                    nq.append(nx)
            q = nq
