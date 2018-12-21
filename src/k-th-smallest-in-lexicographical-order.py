import math


class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        k -= 1
        nText = str(n)
        rangeSize = self.getFullRangeSize(len(nText))
        up = int(nText[0])
        i = 1
        while i < up and k >= rangeSize:
            k -= rangeSize
            i += 1
        if i < up:
            return int(str(i) + self.findInFullRange(len(nText) - 1, k))
        rangeSizeUp = self.getPartRangeSize(nText)
        if k < rangeSizeUp:
            return int(str(up) + self.findInPartRange(nText[1:], k))
        k -= rangeSizeUp
        rangeSize = int(rangeSize / 10)
        i = up + 1
        while k >= rangeSize:
            k -= rangeSize
            i += 1
        return int(str(i) + self.findInFullRange(len(nText) - 2, k))

    def findInPartRange(self, nText, k):
        if k == 0:
            return ''
        k -= 1
        rangeSize = self.getFullRangeSize(len(nText))
        up = int(nText[0])
        for i in range(up):
            if k < rangeSize:
                return str(i) + self.findInFullRange(len(nText) - 1, k)
            k -= rangeSize
        partRangeSize = self.getPartRangeSize(nText)
        if k < partRangeSize:
            return str(up) + self.findInPartRange(nText[1:], k)
        k -= partRangeSize
        rangeSize = int(rangeSize / 10)
        i = up + 1
        while k >= rangeSize:
            k -= rangeSize
            i += 1
        return str(i) + self.findInFullRange(len(nText) - 2, k)

    def findInFullRange(self, digits, k):
        if k == 0:
            return ''
        k -= 1
        rangeSize = self.getFullRangeSize(digits)
        return str(int(k / rangeSize)) + \
            self.findInFullRange(digits - 1, k % rangeSize)

    def getFullRangeSize(self, digits):
        return int('1' * digits)

    def getPartRangeSize(self, nText):
        if len(nText) == 1:
            return 1
        nnText = nText[1:]
        up = int(nnText[0])
        size = 1 + self.getFullRangeSize(len(nnText)) * \
            up + self.getPartRangeSize(nnText)
        if len(nnText) > 1:
            size += self.getFullRangeSize(len(nnText) - 1) * (9 - up)
        return size


sol = Solution()
# ret = sol.findKthNumber(13, 2)
# ret = sol.findKthNumber(10, 3)
ret = sol.findKthNumber(100, 10)
print(ret)
