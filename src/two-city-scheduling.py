import math


class Solution:
    def twoCitySchedCost(self, costs) -> int:
        M = len(costs)
        N = M // 2
        total = sum(a for a, _ in costs)
        diff = [(a - b) for a, b in costs]
        diff.sort(reverse = True)
        for i in range(N):
            total -= diff[i]
        return total

    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    #     M = len(costs)
    #     N = M // 2

    #     def helper(i, curSum, countA, countB):
    #         if countA == N and countB == N:
    #             return curSum
    #         if countA == N:
    #             return helper(
    #                 i + 1, curSum + costs[i][1], countA, countB + 1)
    #         elif countB == N:
    #             return helper(
    #                 i + 1, curSum + costs[i][0], countA + 1, countB)
    #         else:
    #             return min(helper(i + 1, curSum + costs[i][1], countA, countB + 1),
    #                        helper(i + 1, curSum + costs[i][0], countA + 1, countB))

    #     return helper(0, 0, 0, 0)

    # def twoCitySchedCost1(self, costs: List[List[int]]) -> int:
    #     M = len(costs)
    #     N = M // 2
    #     cache = dict()

    #     def helper(i, curSum, countA, countB):
    #         if countA == N and countB == N:
    #             return curSum
    #         if (i, curSum, countA, countB) in cache:
    #             return cache[(i, curSum, countA, countB)]
    #         if countA == N:
    #             cache[(i, curSum, countA, countB)] = helper(
    #                 i + 1, curSum + costs[i][1], countA, countB + 1)
    #         elif countB == N:
    #             cache[(i, curSum, countA, countB)] = helper(
    #                 i + 1, curSum + costs[i][0], countA + 1, countB)
    #         else:
    #             cache[(i, curSum, countA, countB)] = min(helper(i + 1, curSum + costs[i][1], countA, countB + 1),
    #                                                      helper(i + 1, curSum + costs[i][0], countA + 1, countB))
    #         return cache[(i, curSum, countA, countB)]

    #     return helper(0, 0, 0, 0)

sol = Solution()
ret = sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print(ret)
ret = sol.twoCitySchedCost([[841,185],[295,946],[928,450],[55,806],[714,89],[787,380],[663,323],[814,265],[581,581],[850,486],[390,491],[560,678],[311,283],[145,772],[987,471],[465,611],[926,367],[782,532],[299,317],[605,260],[751,735],[614,746],[747,904],[267,653]])
print(ret)