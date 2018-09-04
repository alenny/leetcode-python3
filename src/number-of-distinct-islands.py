class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        islandSet = set()
        visited = [[False for c in range(len(grid[0]))]
                   for r in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] or grid[r][c] == 0:
                    continue
                islandSet.add(self.bfs(grid, r, c, visited))
        return len(islandSet)

    def bfs(self, grid, row, col, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(visited)
        cols = len(visited[0])
        visited[row][col] = True
        q = [(row, col)]
        island = ''
        while len(q) > 0:
            nq = []
            for r, c in q:
                island += str(r - row) + ',' + str(c - col) + '|'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                        nq.append((nr, nc))
                        visited[nr][nc] = True
            q = nq
        return island
