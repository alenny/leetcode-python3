from collections import defaultdict
from collections import deque
import math


class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        countMap = defaultdict(int)
        for num in A:
            countMap[num] += 1
        toHandle = deque()
        slots = deque()
        output = 0
        sortedCounts = sorted(countMap.items(), key=lambda itm: itm[0])
        prevNum = sortedCounts[0][0]
        for num, count in sortedCounts:
            for slot in range(prevNum + 1, num):
                slots.append(slot)
            while toHandle and slots:
                output += slots.popleft() - toHandle.popleft()
            slots.clear()
            for _ in range(count - 1):
                toHandle.append(num)
            prevNum = num
        slot = prevNum + 1
        while toHandle:
            output += slot - toHandle.popleft()
            slot += 1
        return output


sol = Solution()
ret = sol.minIncrementForUnique([1, 1, 2, 0])
