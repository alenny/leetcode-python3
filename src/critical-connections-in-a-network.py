import sys

from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # an edge is non-critical when and only when this edge is in a circle

        edges = defaultdict(list)
        candidates = set()
        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)
            candidates.add((min(a, b), max(a, b)))
        path = []
        pathDict = {}
        visited = set()

        # returns the path index of the first node in a circle containing the current node
        def dfs(node):
            prevNode = path[-1] if path else None
            visited.add(node)
            curIdx = pathDict[node] = len(path)
            path.append(node)
            firstIdxInPath = len(path)
            for nextNode in edges[node]:
                if nextNode == prevNode:
                    continue
                if nextNode in pathDict:
                    firstIdxInPath = min(firstIdxInPath, pathDict[nextNode])
                    candidates.discard((min(node, nextNode), max(node, nextNode)))
                    continue
                if not nextNode in visited:
                    firstIdxInPath = min(firstIdxInPath, dfs(nextNode))    
            if firstIdxInPath < curIdx:
                candidates.discard((min(node, prevNode), max(node, prevNode)))
            pathDict.pop(node)
            path.pop()
            return firstIdxInPath

        dfs(0)
        return list(candidates)

sys.setrecursionlimit(200000)
sol = Solution()
ret = sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
# ret = sol.criticalConnections(10, [[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]])
print(len(ret))
# print(ret)