class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    area += 2
                area += max(0,
                            grid[r - 1][c] - grid[r][c]) if r > 0 else grid[r][c]
                area += max(0,
                            grid[r + 1][c] - grid[r][c]) if r < rows - 1 else grid[r][c]
                area += max(0,
                            grid[r][c - 1] - grid[r][c]) if c > 0 else grid[r][c]
                area += max(0,
                            grid[r][c + 1] - grid[r][c]) if c < cols - 1 else grid[r][c]
        return area
