class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return
        self.bfs(rooms)

    def bfs(self, rooms):
        rows = len(rooms)
        cols = len(rooms[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[False for c in range(cols)] for r in range(rows)]
        q = []
        # put all gates in the initial queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = True
        dist = 0
        while len(q) > 0:
            nq = []
            for cr, cc in q:
                if rooms[cr][cc] < 0:
                    continue
                rooms[cr][cc] = min(rooms[cr][cc], dist)
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or visited[nr][nc] or rooms[nr][nc] < 0:
                        continue
                    visited[nr][nc] = True
                    nq.append((nr, nc))
            q = nq
            dist += 1


sol = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
sol.wallsAndGates(rooms)
print('ok')
