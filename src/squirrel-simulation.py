import math


class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        distance = 0
        maxSavedLength = -math.inf
        for nut in nuts:
            nutToTree = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            distance += 2 * nutToTree
            savedLength = nutToTree - \
                (abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1]))
            if savedLength > maxSavedLength:
                maxSavedLength = savedLength
        return distance - maxSavedLength


sol = Solution()
ret = sol.minDistance(5, 5, [3, 2], [0, 1], [[2, 0], [4, 1], [0, 4], [1, 3], [1, 0], [3, 4], [3, 0], [
                      2, 3], [0, 2], [0, 0], [2, 2], [4, 2], [3, 3], [4, 4], [4, 0], [4, 3], [3, 1], [2, 1], [1, 4], [2, 4]])
print(ret)
