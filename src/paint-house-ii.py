import math


class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prevResult = [(0, -1), (0, -1)]
        for row in costs:
            curResult = []
            minThree = self.findMinThree(row if len(row) > 2 else row + [math.inf])
            if prevResult[0][1] != minThree[0][1]:
                curResult.append((prevResult[0][0] + minThree[0][0], minThree[0][1]))
                if prevResult[0][1] != minThree[1][1]:
                    curResult.append((prevResult[0][0] + minThree[1][0], minThree[1][1]))
                elif prevResult[0][0] + minThree[2][0] < prevResult[1][0] + minThree[1][0]:
                    curResult.append((prevResult[0][0] + minThree[2][0], minThree[2][1]))
                else:
                    curResult.append((prevResult[1][0] + minThree[1][0], minThree[1][1]))
            elif prevResult[1][0] + minThree[0][0] < prevResult[0][0] + minThree[1][0]:
                    curResult.append((prevResult[1][0] + minThree[0][0], minThree[0][1]))
                    curResult.append((prevResult[0][0] + minThree[1][0], minThree[1][1]))
            else:
                curResult.append((prevResult[0][0] + minThree[1][0], minThree[1][1]))
                if prevResult[0][0] + minThree[2][0] < prevResult[1][0] + minThree[0][0]:
                    curResult.append((prevResult[0][0] + minThree[2][0], minThree[2][1]))
                else:
                    curResult.append((prevResult[1][0] + minThree[0][0], minThree[0][1]))
            prevResult = curResult
        return prevResult[0][0]

    def findMinThree(self, arr):
        ret = [(math.inf, -1) for i in range(3)]
        for i, val in enumerate(arr):
            if val < ret[0][0]:
                ret[0], ret[1], ret[2] = (val, i), ret[0], ret[1]
            elif val < ret[1][0]:
                ret[1], ret[2] = (val, i), ret[1]
            elif val < ret[2][0]:
                ret[2] = (val, i)
        return ret

sol = Solution()
# ret =sol.minCostII([[20,7,7,5,12],[3,19,9,4,15],[2,16,8,17,15],[7,3,8,11,13],[3,14,19,2,17],[11,19,17,6,1],[4,2,11,12,6],[9,2,9,15,1],[5,7,3,20,14],[3,20,7,8,11],[1,12,2,2,2],[14,17,15,10,9],[10,12,9,19,20],[4,6,10,3,10],[7,3,10,4,12],[7,2,8,6,4],[3,10,5,9,10],[7,12,1,12,12],[20,17,19,1,10],[13,2,7,20,2],[13,8,18,13,2]])
# ret = sol.minCostII([[3,20,7,7,16,8,7,12,11,19,1],[10,14,3,3,9,13,4,12,14,13,1],[10,1,14,11,1,16,2,7,16,7,19],[13,20,17,15,3,13,8,10,7,8,9],[4,14,18,15,11,9,19,3,15,12,15],[14,12,16,19,2,12,13,3,11,10,9],[18,12,10,16,19,9,18,4,14,2,4]])
ret = sol.minCostII([[8,16,12,18,9],[19,18,8,2,8],[8,5,5,13,4],[15,9,3,19,2],[8,7,1,8,17],[8,2,8,15,5],[8,17,1,15,3],[8,8,5,5,16],[2,2,18,2,9]])
print(ret)