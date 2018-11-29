class Solution:

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # smart solution as the below:
        # https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
        xMap = [set() for x in range(10000)]
        yMap = [set() for y in range(10000)]
        for i, (sx, sy) in enumerate(stones):
            xMap[sx].add(i)
            yMap[sy].add(i)
        # count the number of connected graphs
        # in each connected graph, there will always be one stone left
        # so totally we can remove len(stones) - (number of connected graphs)
        visited = [False] * len(stones)
        graphCount = 0
        for i, (sx, sy) in enumerate(stones):
            if visited[i]:
                continue
            graphCount += 1
            self.bfs(stones, visited, xMap, yMap, i)
        return len(stones) - graphCount

    def bfs(self, stones, visited, xMap, yMap, i):
        q = [i]
        visited[i] = True
        while len(q) > 0:
            nq = []
            for i in q:
                sx, sy = stones[i]
                maps = [xMap[sx], yMap[sy]]
                for mp in maps:
                    for j in mp:
                        if j == i or visited[j]:
                            continue
                        visited[j] = True
                        nq.append(j)
            q = nq


sol = Solution()
ret = sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
print(ret)
