class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min0, min0Idx = 10001, []
        min1, min1Idx = 10001, []
        max0, max0Idx = -10001, []
        max1, max1Idx = -10001, []
        for i in range(len(arrays)):
            mi, ma = arrays[i][0], arrays[i][-1]
            if mi < min0:
                min1, min1Idx = min0, min0Idx
                min0, min0Idx = mi, [i]
            elif mi == min0:
                min0Idx.append(i)
            elif mi < min1:
                min1, min1Idx = mi, [i]
            elif mi == min1:
                min1Idx.append(i)
            if ma > max0:
                max1, max1Idx = max0, max0Idx
                max0, max0Idx = ma, [i]
            elif ma == max0:
                max0Idx.append(i)
            elif ma > max1:
                max1, max1Idx = ma, [i]
            if ma == max1:
                max1Idx.append(i)
        if len(min0Idx) > 1 or len(max0Idx) > 1 or min0Idx[0] != max0Idx[0]:
            return max0 - min0
        return max(max1 - min0, max0 - min1)
