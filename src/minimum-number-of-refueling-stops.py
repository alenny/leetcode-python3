import heapq


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # greedy and max heap
        stations += [[target, 0]]
        maxHeap = []
        curFuel = startFuel
        stops = 0
        prevPos = 0
        for pos, fuel in stations:
            curFuel -= (pos - prevPos)
            while curFuel < 0 and len(maxHeap) > 0:
                curFuel -= heapq.heappop(maxHeap)
                stops += 1
            if curFuel < 0:
                return -1
            heapq.heappush(maxHeap, -fuel)
            prevPos = pos
        return stops if curFuel >= 0 else -1

    def minRefuelStopsDP(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # dp[i] means the max distance the car can arrive at by refueling at i stops
        # so the ith stop must be within dp[i - 1] to avoid out of fuel
        # when the first time dp[i] exceeds target, i is the result
        dp = [0 for i in range(len(stations) + 1)]
        dp[0] = startFuel
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] < pos:
                    break
                dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1


sol = Solution()
# ret = sol.minRefuelStops(100, 1, [[10, 100]])
# ret = sol.minRefuelStops(100, 50, [[25, 25], [50, 50]])
ret = sol.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])
# ret = sol.minRefuelStops(1000, 83, [[25, 27], [36, 187], [140, 186], [378, 6], [
#                          492, 202], [517, 89], [579, 234], [673, 86], [808, 53], [954, 49]])
print(ret)
