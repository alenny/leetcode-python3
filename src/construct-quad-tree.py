# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        return self.__getNode(self.__constructHelper(grid, 0, 0, len(grid)))

    def __constructHelper(self, grid, r, c, size):
        if size == 1:
            return grid[r][c]
        halfSize = size >> 1
        topLeft = self.__constructHelper(grid, r, c, halfSize)
        topRight = self.__constructHelper(grid, r, c + halfSize, halfSize)
        bottomLeft = self.__constructHelper(grid, r + halfSize, c, halfSize)
        bottomRight = self.__constructHelper(
            grid, r + halfSize, c + halfSize, halfSize)
        if topLeft == topRight and topRight == bottomLeft and bottomLeft == bottomRight:
            return topLeft
        return Node(None, False,
                    self.__getNode(topLeft), self.__getNode(topRight),
                    self.__getNode(bottomLeft), self.__getNode(bottomRight))

    def __getNode(self, result):
        return result if isinstance(result, Node) else Node(bool(result), True, None, None, None, None)
