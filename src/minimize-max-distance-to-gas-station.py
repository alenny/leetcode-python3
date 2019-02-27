import math
import heapq


class Solution:
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # return self.minmaxGasDistByHeap(stations, K)
        return self.minmaxGasDistByBinarySearch(stations, K)

    def minmaxGasDistByBinarySearch(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        bias = 10**-6
        N = len(stations)
        minDist, maxDist = 0, stations[N - 1] - stations[0]
        while minDist + bias < maxDist:
            midDist = (minDist + maxDist) / 2
            inserted = 0
            for i in range(1, N):
                dist = stations[i] - stations[i - 1]
                inserted += math.ceil(dist / midDist) - 1
            if inserted > K:
                minDist = midDist
            else:
                maxDist = midDist
        return minDist

    def minmaxGasDistByHeap(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        N = len(stations)
        totalDist = stations[-1] - stations[0]
        buckets = K + N - 1
        # Note avgDist is the minimum possible result
        # so any gap less than or equal to avgDist need not be split
        avgDist = totalDist / buckets
        maxHeap = []
        sumGap = 0
        gapsToHandle = []
        for i in range(1, N):
            gap = stations[i] - stations[i - 1]
            parts = gap / avgDist
            if parts <= 1:
                continue
            sumGap += gap
            gapsToHandle.append(gap)
        for gap in gapsToHandle:
            # maxParts = int(gap / avgDist)
            # inserted = min(maxParts - 1, int(gap / sumGap * K))
            inserted = int(gap / sumGap * K)
            dist = gap / (inserted + 1)
            heapq.heappush(maxHeap, (-dist, inserted, -gap))
            K -= inserted
        while K > 0:
            top = heapq.heappop(maxHeap)
            inserted, gap = top[1], -top[2]
            inserted += 1
            dist = gap / (inserted + 1)
            heapq.heappush(maxHeap, (-dist, inserted, -gap))
            K -= 1
        return -maxHeap[0][0]


sol = Solution()
# ret = sol.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
# ret = sol.minmaxGasDist([23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1)
# ret = sol.minmaxGasDist([16, 22, 29, 33, 34, 54, 57, 71, 84, 98], 25)
# ret = sol.minmaxGasDist([2, 7, 12, 29, 41, 42, 53, 54, 62, 92], 11)
ret = sol.minmaxGasDist([12, 17, 54, 66, 77, 83, 88, 92, 97, 99], 6)  # 7.4
# ret = sol.minmaxGasDist(
#     [10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3)     # 9.66667
print(ret)
