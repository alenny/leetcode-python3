import math


class PathInfo:
    def __init__(self):
        self.length = math.inf
        self.path = ''

    def newPath(self, length, path):
        if length > self.length or length == self.length and path > self.path:
            return False
        self.length = length
        self.path = path
        return True


class Solution:
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        destR, destC = hole
        directions = [('u', -1, 0),  ('d', 1, 0),  ('l', 0, -1),  ('r', 0, 1)]
        rows = len(maze)
        cols = len(maze[0])
        paths = [[PathInfo() for c in range(cols)] for r in range(rows)]
        spots = [(ball[0], ball[1])]
        paths[ball[0]][ball[1]].length = 0
        while len(spots) > 0:
            nextSpots = []
            nsSet = set()
            for r, c in spots:
                for direct, dr, dc in directions:
                    path = paths[r][c].path + direct
                    nr, nc = r, c
                    while nr >= 0 and nr < rows and nc >= 0 and nc < cols and maze[nr][nc] == 0 and (nr, nc) != (destR, destC):
                        nr += dr
                        nc += dc
                    if (nr, nc) == (destR, destC):
                        paths[nr][nc].newPath(
                            paths[r][c].length + abs(nr - r) + abs(nc - c), path)
                        continue
                    nr -= dr
                    nc -= dc
                    if not paths[nr][nc].newPath(paths[r][c].length + abs(nr - r) + abs(nc - c), path):
                        continue
                    key = str(nr) + ',' + str(nc)
                    if key in nsSet:
                        continue
                    nextSpots.append((nr, nc))
                    nsSet.add(key)
            spots = nextSpots
        return paths[destR][destC].path if paths[destR][destC].length < math.inf else 'impossible'


sol = Solution()
# ret = sol.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [
#                           0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1])
ret = sol.findShortestWay([[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]],
                          [0, 4],
                          [3, 5])
print(ret)
