import math


class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # calculate distance between any two nodes
        N = len(graph)
        distMap = [[[] for j in range(N)] for i in range(N)]
        for node in range(N):
            self.bfsCalDist(graph, node, distMap)
        shortest = math.inf
        cache = [dict() for i in range(N)]
        for node in range(N):
            shortest = min(shortest,
                           self.dfsTraverse(distMap, node, set([node]), cache))
        return shortest

    def bfsCalDist(self, graph, node, distMap):
        N = len(graph)
        q = [node]
        visited = [False for i in range(N)]
        visited[node] = True
        distance = 0
        while len(q) > 0:
            nq = []
            for cur in q:
                distMap[node][distance].append(cur)
                for nxt in graph[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
            distance += 1

    def dfsTraverse(self, distMap, node, visitedSet, cache):
        N = len(distMap)
        if len(visitedSet) == N:
            return 0
        key = self.getCacheKey(visitedSet)
        if key in cache[node]:
            return cache[node][key]
        shortest = math.inf
        handled = False
        for dist in range(1, N):
            nextNodes = distMap[node][dist]
            if len(nextNodes) == 0:
                break
            for nxt in nextNodes:
                if nxt in visitedSet:
                    continue
                handled = True
                visitedSet.add(nxt)
                shortest = min(shortest,
                               self.dfsTraverse(distMap, nxt, visitedSet, cache) + dist)
                visitedSet.remove(nxt)
            if handled:
                break
        cache[node][key] = shortest
        return shortest

    def getCacheKey(self, visitedSet):
        l = list(visitedSet)
        l.sort()
        return str(l)


sol = Solution()
# ret = sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
# ret = sol.shortestPathLength([[1, 2, 3], [0], [0], [0]])
# ret = sol.shortestPathLength([[2], [2, 8], [0, 1, 3, 4], [2],
#                               [2], [8, 6], [5], [8], [1, 5, 7]])
ret = sol.shortestPathLength([[2, 10], [2, 7], [0, 1, 3, 4, 5, 8], [2], [2],
                              [2], [8], [9, 11, 8, 1], [7, 6, 2], [7], [11, 0], [7, 10]])
print(ret)
