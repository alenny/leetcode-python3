from collections import defaultdict
import math


class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balance = defaultdict(int)
        for x, y, z in transactions:
            balance[x] -= z
            balance[y] += z
        posBalance, negBalance = [], []
        for b in balance.values():
            if b > 0:
                posBalance.append(b)
            elif b < 0:
                negBalance.append(b)
        posBalance, negBalance, trans = self.refactorBalance(
            posBalance, negBalance)
        return self.rebalance(posBalance, negBalance, dict()) + trans

    def refactorBalance(self, posBalance, negBalance):
        p2 = []
        nMap = defaultdict(int)
        for nb in negBalance:
            nMap[nb] += 1
        trans = 0
        for pb in posBalance:
            if -pb in nMap:
                if nMap[-pb] == 1:
                    nMap.pop(-pb)
                else:
                    nMap[-pb] -= 1
                trans += 1
            else:
                p2.append(pb)
        n2 = []
        for k, v in nMap.items():
            for i in range(v):
                n2.append(k)
        return p2, n2, trans

    def rebalance(self, posBalance, negBalance, cache):
        cacheKey = self.getCacheKey(posBalance, negBalance)
        if cacheKey in cache:
            return cache[cacheKey]
        if len(posBalance) == 0 and len(negBalance) == 0:
            return 0
        minTrans = math.inf
        for pi, pb in enumerate(posBalance):
            for ni, nb in enumerate(negBalance):
                if pb > -nb:
                    nextPosBalance = posBalance[:]
                    nextPosBalance[pi] += nb
                    nextNegBalance = negBalance[:ni] + negBalance[ni + 1:]
                elif pb < -nb:
                    nextNegBalance = negBalance[:]
                    nextNegBalance[ni] += pb
                    nextPosBalance = posBalance[:pi] + posBalance[pi + 1:]
                else:
                    nextPosBalance = posBalance[:pi] + posBalance[pi + 1:]
                    nextNegBalance = negBalance[:ni] + negBalance[ni + 1:]
                minTrans = min(minTrans,
                               self.rebalance(nextPosBalance, nextNegBalance, cache))
        minTrans += 1
        cache[cacheKey] = minTrans
        return minTrans

    def getCacheKey(self, posBalance, negBalance):
        p, n = posBalance[:], negBalance[:]
        p.sort()
        n.sort()
        return str(n + p)


sol = Solution()
# ret = sol.minTransfers([[1, 5, 8], [8, 9, 8], [2, 3, 9], [4, 3, 1]])
ret = sol.minTransfers([[0, 1, 10], [2, 0, 5]])
# ret = sol.minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]])
# ret = sol.minTransfers([[1, 8, 1], [1, 13, 21], [2, 8, 10], [3, 9, 20], [
#                        4, 10, 61], [5, 11, 61], [6, 12, 59], [7, 13, 60]])  # 8
# ret = sol.minTransfers([[10, 11, 6], [12, 13, 7], [14, 15, 2], [
#                        14, 16, 2], [14, 17, 2], [14, 18, 2]])   # 6
print(ret)
