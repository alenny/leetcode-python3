import math


class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        destR, destC = destination
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(maze)
        cols = len(maze[0])
        distances = [[math.inf for c in range(cols)] for r in range(rows)]
        spots = [(start[0], start[1])]
        distances[start[0]][start[1]] = 0
        while len(spots) > 0:
            nextSpots = []
            nsSet = set()
            for r, c in spots:
                for dr, dc in directions:
                    nr, nc = r, c
                    while nr >= 0 and nr < rows and nc >= 0 and nc < cols and maze[nr][nc] == 0:
                        nr += dr
                        nc += dc
                    nr -= dr
                    nc -= dc
                    dist = distances[r][c] + abs(nr - r) + abs(nc - c)
                    if nr == destR and nc == destC:
                        distances[destR][destC] = min(
                            distances[destR][destC], dist)
                        continue
                    if dist >= distances[nr][nc]:
                        continue
                    distances[nr][nc] = dist
                    key = str(nr) + ',' + str(nc)
                    if key in nsSet:
                        continue
                    nextSpots.append((nr, nc))
                    nsSet.add(key)
            spots = nextSpots
        return distances[destR][destC] if distances[destR][destC] != math.inf else -1


sol = Solution()
ret = sol.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [
                           1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4])
print(ret)
