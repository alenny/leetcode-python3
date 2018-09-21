class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(maze)
        cols = len(maze[0])
        visited = [[False for c in range(cols)] for r in range(rows)]
        spots = [(start[0], start[1])]
        visited[start[0]][start[1]] = True
        while len(spots) > 0:
            nextSpots = []
            for r, c in spots:
                for dr, dc in directions:
                    nr, nc = r, c
                    while nr >= 0 and nr < rows and nc >= 0 and nc < cols and maze[nr][nc] == 0:
                        nr += dr
                        nc += dc
                    nr -= dr
                    nc -= dc
                    if visited[nr][nc]:
                        continue
                    if nr == destination[0] and nc == destination[1]:
                        return True
                    nextSpots.append((nr, nc))
                    visited[nr][nc] = True
            spots = nextSpots
        return False
