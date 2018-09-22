import random
import math


class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.squareR = radius * radius
        self.cx = x_center
        self.cy = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # Must use sqrt here to have better randomization
        # see: https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/155650/Explanation-with-Graphs-why-using-Math.sqrt()
        distToCenter = math.sqrt(random.uniform(0, 1)) * self.r
        degree = random.uniform(0, 2) * math.pi
        return [self.cx + distToCenter * math.sin(degree), self.cy + distToCenter * math.cos(degree)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


sol = Solution(0.01, -73839.1, -3289891.3)
ret = sol.randPoint()
ret = sol.randPoint()
