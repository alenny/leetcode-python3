class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 3:
            return True
        dx1, dy1 = points[1][0] - points[0][0], points[1][1] - points[0][1]
        dx2, dy2 = points[2][0] - points[1][0], points[2][1] - points[1][1]
        turnState = self.getTurnState(dx1, dy1, dx2, dy2)
        prevDx, prevDy = dx2, dy2
        for j in range(3, len(points) + 2):
            # loop to compare points[0] - points[-1] and points[1] - points[0]
            i = j % len(points)
            dxi, dyi = points[i][0] - \
                points[i - 1][0], points[i][1] - points[i - 1][1]
            curTurnState = self.getTurnState(prevDx, prevDy, dxi, dyi)
            if turnState != 0 and curTurnState != 0 and turnState != curTurnState:
                return False
            if turnState == 0 and curTurnState != 0:
                turnState = curTurnState
            prevDx, prevDy = dxi, dyi
        return turnState != 0

    # return 0 if no turn, 1 if turn clockwise, -1 if turn counterclockwise
    def getTurnState(self, dx1, dy1, dx2, dy2):
        left = dy2 * dx1
        right = dy1 * dx2
        return 0 if left == right else (1 if left < right else -1)


sol = Solution()
ret = sol.isConvex([[0, 0], [0, 1], [1, 1], [1, 0]])
ret = sol.isConvex([[0, 0], [1, 0], [1, 1], [-1, 1], [-1, 0]])
ret = sol.isConvex([[0, 0], [1, 1], [0, 2], [-1, 2], [0, 1]])
print(ret)
