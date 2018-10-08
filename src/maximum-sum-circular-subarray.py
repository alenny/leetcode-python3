import math


class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minSumToCur, maxSumToCur = 0, 0
        globalMinSum, globalMaxSum = math.inf, -math.inf
        totalSum = 0
        for i in range(len(A) - 1):
            a = A[i]
            totalSum += a
            minSumToCur = min(minSumToCur + a, a)
            globalMinSum = min(minSumToCur, globalMinSum)
            maxSumToCur = max(maxSumToCur + a, a)
            globalMaxSum = max(maxSumToCur, globalMaxSum)
        totalSum += A[-1]
        return max(globalMaxSum, totalSum, totalSum - globalMinSum)


sol = Solution()
ret = sol.maxSubarraySumCircular([-3, -5, -2, -5, -6])
print(ret)
