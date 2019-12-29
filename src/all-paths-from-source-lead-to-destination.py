from typing import List
from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        edgeMap = defaultdict(set)
        for s, d in edges:
            edgeMap[s].add(d)
        if destination in edgeMap:
            return False

        def dfs(cur, path, pathSet: set):
            if cur in pathSet:
                return False    # loop
            if cur == destination:
                return True
            if not cur in edgeMap:
                return False    # node has no outgoing edge
            if cur in visited:
                return True
            visited.add(cur)
            path.append(cur)
            pathSet.add(cur)
            for dest in edgeMap[cur]:
                if not dfs(dest, path, pathSet):
                    return False
            pathSet.remove(cur)
            path.pop()
            return True

        return dfs(source, [], set())
