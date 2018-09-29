class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        limit = pow(2, 31) - 1
        l, r = 0, 10000
        while l <= r:
            mid = l + r >> 1
            x = reader.get(mid)
            if x == target:
                return mid
            if x > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
