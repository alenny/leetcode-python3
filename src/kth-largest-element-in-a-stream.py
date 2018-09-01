import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # always track the k largest numbers in the min-heap and the heap[0] is the answer
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

kl = KthLargest(3, [4, 5, 8, 2])
ret = kl.add(3)
ret = kl.add(5)
ret = kl.add(10)
ret = kl.add(9)
ret = kl.add(4)
