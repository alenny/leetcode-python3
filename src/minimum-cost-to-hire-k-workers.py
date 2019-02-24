import heapq
import math


class Person:
    def __init__(self, quality, wage):
        self.quality = quality
        self.wage = wage
        self.ratio = wage / quality


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        persons = [Person(q, w) for q, w in zip(quality, wage)]
        persons.sort(key=lambda p: p.ratio)
        maxHeap = []
        totalQualityInHeap = 0
        minCost = math.inf
        for p in persons:
            if len(maxHeap) < K - 1:
                heapq.heappush(maxHeap, -p.quality)
                totalQualityInHeap += p.quality
                continue
            minCost = min(minCost, (p.quality + totalQualityInHeap) * p.ratio)
            if not maxHeap or p.quality >= -maxHeap[0]:
                continue
            totalQualityInHeap += p.quality + maxHeap[0]
            heapq.heappushpop(maxHeap, -p.quality)
        return minCost


sol = Solution()
# ret = sol.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2)
ret = sol.mincostToHireWorkers([32, 43, 66, 9, 94, 57, 25, 44, 99, 19], [
                               187, 366, 117, 363, 121, 494, 348, 382, 385, 262], 4)
# ret = sol.mincostToHireWorkers(
#     [39, 79, 78, 16, 6, 36, 97, 79, 27, 14, 31, 4, 36, 2, 61, 30, 74, 35, 65, 31],
#     [213, 456, 71, 53, 110, 376, 403, 273, 358, 457,
#         47, 427, 123, 316, 140, 60, 213, 48, 269, 132],
#     4)
print(ret)
