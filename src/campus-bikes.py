# import heapq
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        nw = len(workers)

        def calDist(x0, y0, x1, y1):
            return abs(x0 - x1) + abs(y0 - y1)

        heap = []
        for wi, (wx, wy) in enumerate(workers):
            for bi, (bx, by) in enumerate(bikes):
                dist = calDist(wx, wy, bx, by)
                heap.append((dist, wi, bi))
                # heapq.heappush(heap, (dist, wi, bi))
        heap.sort()
        ret = [0] * nw
        workerAssigned = set()
        bikeAssigned = set()
        i = 0
        while len(workerAssigned) < nw:
            while True:
                _, wi, bi = heap[i]
                i += 1
                # _, wi, bi = heapq.heappop(heap)
                if (not wi in workerAssigned and not bi in bikeAssigned):
                    ret[wi] = bi
                    workerAssigned.add(wi)
                    bikeAssigned.add(bi)
                    break
        return ret

sol = Solution()
ret = sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])
print(ret)