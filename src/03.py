from typing import List
import math


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # DP
        AL = len(A)
        dp = [[math.inf] * AL for _ in range(AL)]
        for i in range(AL - 1):
            dp[i][i + 1] = 0
        for dist in range(2, AL):
            for i in range(AL - dist):
                j = i + dist
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + A[i] * A[j] * A[k] + dp[k][j])
        return dp[0][AL - 1]

    def minScoreTriangulationBT(self, A: List[int]) -> int:
        AL = len(A)
        cache = dict()

        def getKey(indexes):
            key = 0
            for idx in indexes:
                key |= (1 << idx)
            return key

        def backTrack(indexes):
            key = getKey(indexes)
            if key in cache:
                return cache[key]
            N = len(indexes)
            if N == 3:
                cache[key] = A[indexes[0]] * A[indexes[1]] * A[indexes[2]]
                return cache[key]
            minScore = math.inf
            # when the first node is split
            for i in range(2, N - 1):
                minScore = min(minScore,
                               backTrack(indexes[:i + 1]) +
                               backTrack([indexes[0]] + indexes[i:]))
            # when the first node is not split
            minScore = min(minScore,
                           backTrack([indexes[-1], indexes[0], indexes[1]]) +
                           backTrack(indexes[1:]))
            cache[key] = minScore
            return minScore

        ret = backTrack(list(range(AL)))
        return ret


sol = Solution()
# ret = sol.minScoreTriangulation([3, 7, 4, 5])  # 144
# print(ret)
# ret = sol.minScoreTriangulation([6, 6, 2, 5, 5, 5])  # 232
# print(ret)
# ret = sol.minScoreTriangulation([1, 3, 1, 4, 1, 5])  # 13
# print(ret)
# ret = sol.minScoreTriangulation(
#     [35, 73, 90, 27, 71, 80, 21, 33, 33, 13])
# ret = sol.minScoreTriangulation(
#     [35, 73, 90, 27, 71, 80, 21, 33, 33, 13, 48, 12, 68, 70, 80, 36, 66, 3, 70, 58])
ret = sol.minScoreTriangulation([33, 68, 52, 66, 94, 97, 52, 41, 94, 4, 62, 45, 92, 24, 94, 94, 6, 42, 25, 95, 98, 83, 12,
                                 4, 31, 50, 95, 76, 39, 15, 64, 63, 77, 11, 76, 34, 67, 52, 90, 23, 38, 59, 39, 74, 90, 48, 39, 39, 57, 38])   # 602212
print(ret)
