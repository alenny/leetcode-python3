from collections import defaultdict


class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        posMap = defaultdict(list)
        for i in range(len(A)):
            posMap[A[i]].append(i)
        items = list(posMap.items())
        items.sort(key=lambda itm: itm[0])
        totalSmaller = 0
        maxIdx = 0
        i = 0
        while i < len(items):
            for idx in items[i][1]:
                totalSmaller += 1
                maxIdx = max(maxIdx, idx)
                if maxIdx < totalSmaller:
                    return totalSmaller
            i += 1
