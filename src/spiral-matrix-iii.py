class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ret = [[r0, c0]]
        currPos = [r0, c0]
        stepStride = [0, 1]
        stepEnd = [r0, c0 + 1]
        total = R * C
        while len(ret) < total:
            self.doStep(R, C, currPos, stepStride, stepEnd, ret)
        return ret

    def doStep(self, R, C, currPos, stepStride, stepEnd, ret):
        step = self.getStep(stepStride)
        currPos[0] += step[0]
        currPos[1] += step[1]
        if ((currPos[0] < 0 or currPos[0] >= R) and step[0] == 0) or ((currPos[1] < 0 or currPos[1] >= C) and step[1] == 0):
            currPos[0], currPos[1] = stepEnd[0], stepEnd[1]
            self.setNextStride(stepStride, stepEnd)
            return
        if currPos[0] >= 0 and currPos[0] < R and currPos[1] >= 0 and currPos[1] < C:
            ret.append([currPos[0], currPos[1]])
        if (currPos[0] == stepEnd[0] and currPos[1] == stepEnd[1]):
            self.setNextStride(stepStride, stepEnd)

    def setNextStride(self, stepStride, stepEnd):
        if stepStride[0] == 0:
            stepStride[0], stepStride[1] = stepStride[1], 0
        else:
            if stepStride[0] > 0:
                stepStride[1] = -stepStride[0] - 1
            else:
                stepStride[1] = -stepStride[0] + 1
            stepStride[0] = 0
        stepEnd[0] += stepStride[0]
        stepEnd[1] += stepStride[1]

    def getStep(self, stepStride):
        step = [0, 0]
        if stepStride[0] > 0:
            step[0] = 1
        elif stepStride[0] < 0:
            step[0] = -1
        elif stepStride[1] > 0:
            step[1] = 1
        else:
            step[1] = -1
        return step


sol = Solution()
ret = sol.spiralMatrixIII(1, 4, 0, 0)
