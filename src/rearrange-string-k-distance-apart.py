from collections import defaultdict
from collections import deque
import heapq


class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return self.rearrangeStringByHeapReenter(s, k)

    def rearrangeStringByHeapReenter(self, s, k):
        if k <= 1:
            return s
        countMap = defaultdict(int)
        for ch in s:
            countMap[ch] += 1
        maxHeap = []
        for ch, count in countMap.items():
            heapq.heappush(maxHeap, (-count, ch))
        arr = []
        curQ = deque(maxlen=k)
        N = len(s)
        while len(arr) < N:
            reenterItm = curQ[0] if len(curQ) == k else None
            if reenterItm and reenterItm[0] < 0:
                heapq.heappush(maxHeap, reenterItm)
            if not maxHeap:
                return ''
            itm = heapq.heappop(maxHeap)
            arr.append(itm[1])
            curQ.append((itm[0] + 1, itm[1]))
        return ''.join(arr)


sol = Solution()
ret = sol.rearrangeString('aabbcc', 3)  # 'abcabc'
ret = sol.rearrangeString('aaabc', 3)  # ''
ret = sol.rearrangeString("aaadbbcc", 2)  # "abacabcd"
print(ret)
