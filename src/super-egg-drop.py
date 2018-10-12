import math


class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        cache = [dict() for k in range(K + 1)]
        return self.helper(K, N, cache)

    def helper(self, k, n, cache):
        if n in cache[k]:
            return cache[k][n]
        if k == 1 or n <= 2:
            return n
        upHalfMin = 1
        upHalfMax = n - 1
        while upHalfMin <= upHalfMax:
            upHalf = upHalfMin + upHalfMax >> 1
            downHalf = n - upHalf - 1
            upTry = self.helper(k, upHalf, cache)
            downTry = self.helper(k - 1, downHalf, cache)
            if upHalfMin == upHalfMax or downTry == upTry:
                break
            if downTry > upTry:
                upHalfMin = upHalf + 1
            else:
                upHalfMax = upHalf - 1
        cache[k][n] = max(upTry, downTry) + 1
        return cache[k][n]


sol = Solution()
# ret = sol.superEggDrop(3, 2)
# ret = sol.superEggDrop(2, 6)
ret = sol.superEggDrop(3, 200)
# ret = sol.superEggDrop(4, 10000)
print(ret)
