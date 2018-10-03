class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        hLen = len(heights)
        while V > 0:
            l = K
            firstSink = K
            while l > 0 and heights[l - 1] <= heights[l]:
                if heights[l - 1] < heights[l]:
                    firstSink = l - 1
                l -= 1
            if firstSink != K:
                heights[firstSink] += 1
                V -= 1
                continue
            # no sink to the left, check right
            r = K
            while r < hLen - 1 and heights[r + 1] <= heights[r]:
                if heights[r + 1] < heights[r]:
                    firstSink = r + 1
                r += 1
            if firstSink != K:
                heights[firstSink] += 1
                V -= 1
                continue
            # no sink to the right either
            heights[K] += 1
            V -= 1
        return heights
