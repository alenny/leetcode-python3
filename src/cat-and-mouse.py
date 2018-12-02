from collections import defaultdict
from collections import deque


class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        # key = (mouse, cat, turn). turn: 1:mouse, 2:cat
        results = defaultdict(int)  # val: 0: draw, 1: mouse win, 2: cat win
        q = deque()
        for c in range(1, N):
            results[(0, c, 2)] = 1
            q.append((0, c, 2, 1))
            results[(c, c, 2)] = results[(c, c, 1)] = 2
            q.append((c, c, 2, 2))
            q.append((c, c, 1, 2))
        children = dict()
        for m in range(N):
            for c in range(1, N):
                children[(m, c, 1)] = len(graph[m])
                children[(m, c, 2)] = len(graph[c]) - (0 in graph[c])
        while q:
            # in q, r won't be 0
            m, c, t, r = q.popleft()
            for pm, pc, pt in self.parents(graph, m, c, t):
                if (pm, pc, pt) in results:
                    continue
                if r == pt:
                    results[(pm, pc, pt)] = r
                    q.append((pm, pc, pt, r))
                else:
                    children[(pm, pc, pt)] -= 1
                    if children[(pm, pc, pt)] == 0:
                        results[(pm, pc, pt)] = r
                        q.append((pm, pc, pt, r))
        return results[(1, 2, 1)]

    def parents(self, graph, m, c, t):
        if t == 1:
            for pc in graph[c]:
                if pc != 0:
                    yield m, pc, 2
        else:
            for pm in graph[m]:
                yield pm, c, 1


sol = Solution()
# ret = sol.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]])
# ret = sol.catMouseGame([[2, 3], [2], [0, 1], [0, 4], [3]])
# ret = sol.catMouseGame([[2, 3, 4], [4], [0, 3], [0, 2], [0, 1]])
# ret = sol.catMouseGame([[6], [4], [9], [5], [1, 5], [3, 4, 6], [
#                        0, 5, 10], [8, 9, 10], [7], [2, 7], [6, 7]])
ret = sol.catMouseGame([[2,9,14],[2,5,7],[0,1,3,8,9,11,14],[2,12],[5,11,18],[1,4,18],[9,17,19],[1,11,12,13,14,17,19],[2,16,17],[0,2,6,12,14,18],[14],[2,4,7],[3,7,9,13],[7,12,14],[0,2,7,9,10,13,17],[18],[8,19],[6,7,8,14,19],[4,5,9,15],[6,7,16,17]])
print(ret)
