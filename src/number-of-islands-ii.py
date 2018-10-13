from collections import defaultdict


class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.nextIsland = 0
        posToIsland = dict()
        islandToPos = defaultdict(list)
        ret = []
        for r, c in positions:
            connectedIslands = set()
            for dr, dc in delta:
                r1, c1 = r + dr, c + dc
                if r1 < 0 or r1 >= m or c1 < 0 or c1 >= n:
                    continue
                key1 = self.getKey(r1, c1)
                if key1 in posToIsland:
                    connectedIslands.add(posToIsland[key1])
            if not connectedIslands:
                self.addNewIsland(posToIsland, islandToPos, r, c)
            else:
                self.mergeIslands(posToIsland, islandToPos,
                                  connectedIslands, r, c)
            ret.append(len(islandToPos))
        return ret

    def mergeIslands(self, posToIsland, islandToPos, connectedIslands, r, c):
        targetIsland = min(connectedIslands)
        for island in connectedIslands:
            if island == targetIsland:
                continue
            poses = islandToPos[island]
            for pos in poses:
                posToIsland[pos] = targetIsland
                islandToPos[targetIsland].append(pos)
            islandToPos.pop(island)
        key = self.getKey(r, c)
        posToIsland[key] = targetIsland
        islandToPos[targetIsland].append(key)

    def addNewIsland(self, posToIsland, islandToPos, r, c):
        key = self.getKey(r, c)
        posToIsland[key] = self.nextIsland
        islandToPos[self.nextIsland].append(key)
        self.nextIsland += 1

######################################################################

    def numIslands2BySurroundings(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0] * n for r in range(m)]
        grid[positions[0][0]][positions[0][1]] = 1
        ret = [1]
        surroundings = [set()]
        self.addSurroundingsToSet(
            grid, positions[0][0], positions[0][1], surroundings[0])
        for i in range(1, len(positions)):
            r, c = positions[i]
            grid[r][c] = 1
            key = self.getKey(r, c)
            newSurroundings = [set()]
            self.addSurroundingsToSet(grid, r, c, newSurroundings[0])
            for i in range(len(surroundings)):
                if key in surroundings[i]:
                    surroundings[i].remove(key)
                    newSurroundings[0] = newSurroundings[0].union(
                        surroundings[i])
                else:
                    newSurroundings.append(surroundings[i])
            surroundings = newSurroundings
            ret.append(len(surroundings))
        return ret

    def addSurroundingsToSet(self, grid, r, c, surroundingSet):
        m, n = len(grid), len(grid[0])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in delta:
            r1, c1 = r + dr, c + dc
            if r1 < 0 or r1 >= m or c1 < 0 or c1 >= n or grid[r1][c1] == 1:
                continue
            surroundingSet.add(self.getKey(r1, c1))

    def getKey(self, r, c):
        return '{0},{1}'.format(r, c)


sol = Solution()
# ret = sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
# ret = sol.numIslands2(3, 3, [[0, 1], [1, 2], [2, 1], [
#                       1, 0], [0, 2], [0, 0], [1, 1]])
ret = sol.numIslands2(9, 9, [[8,5],[8,0],[3,4],[0,3],[1,0],[5,4],[0,8],[5,7],[0,6],[6,2],[4,7],[2,7],[8,7],[8,6],[5,3],[2,3],[3,5],[3,1],[0,2],[8,8],[6,4],[0,1],[0,4],[7,5],[3,0]])
print(ret)
