import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        minHeap = []
        for a in A:
            heapq.heappush(minHeap, a)
        for _ in range(K):
            x = heapq.heappop(minHeap)
            heapq.heappush(minHeap, -x)
        return sum(minHeap)
