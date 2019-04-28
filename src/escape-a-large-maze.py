class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        bl = len(blocked)
        blockedSet = set([(x, y) for x, y in blocked])
        SideLength = 10**6
        MaxSquaresClosed = bl * bl // 2
        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # ret: (inClosedArea, metP1)
        def inClosed(p0, p1):
            q = [(p0[0], p0[1])]
            visited = set(q)
            while q:
                nq = []
                for x, y in q:
                    for dx, dy in deltas:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= SideLength or ny < 0 or ny >= SideLength or (nx, ny) in blockedSet or (nx, ny) in visited:
                            continue
                        if (nx, ny) == (p1[0], p1[1]):
                            return False, True
                        nq.append((nx, ny))
                        visited.add((nx, ny))
                        if len(visited) > MaxSquaresClosed:
                            return False, False
                q = nq
            return True, False

        retSource = inClosed(source, target)
        return retSource[1] or not retSource[0] and not inClosed(target, source)[0]


sol = Solution()
# ret = sol.isEscapePossible([[0, 1], [1, 0]], [0, 0], [0, 2])
# print(ret)
ret = sol.isEscapePossible([], [0, 0], [999999, 999999])
print(ret)
