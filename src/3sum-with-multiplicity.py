from collections import defaultdict


class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        modulo = 10**9 + 7
        mapA = defaultdict(int)
        for i, a in enumerate(A):
            mapA[a] += 1
        diffA = list(mapA.keys())
        diffA.sort()
        N = len(diffA)
        total = 0
        for i, ia in enumerate(diffA):
            if mapA[ia] >= 3 and ia * 3 == target:
                total = (total + self.getCombination(mapA[ia], 3)) % modulo
            if mapA[ia] >= 2:
                remain = target - ia * 2
                if remain > ia and remain in mapA:
                    total = (
                        total + self.getCombination(mapA[ia], 2) * mapA[remain]) % modulo
            j, k = i + 1, N - 1
            while j <= k:
                ja, ka = diffA[j], diffA[k]
                sum3 = ia + ja + ka
                if sum3 > target:
                    k -= 1
                    continue
                if sum3 < target:
                    j += 1
                    continue
                if j == k and mapA[ja] < 2:
                    break
                total = (total + mapA[ia] * self.getCombination(mapA[ja], 2)) % modulo \
                    if j == k else (total + mapA[ia] * mapA[ja] * mapA[ka]) % modulo
                k -= 1
                j += 1
        return total

    def getCombination(self, n, m):
        big = max(m, n - m)
        small = n - big
        up = 1
        for x in range(big + 1, n + 1):
            up *= x
        down = 1
        for x in range(2, small + 1):
            down *= x
        return int(up / down)


sol = Solution()
# ret = sol.threeSumMulti([0] * 3000, 0)
# ret = sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
# ret = sol.threeSumMulti([1, 1, 2, 2, 2, 2], 5)
ret = sol.threeSumMulti([1, 2, 3, 3, 1], 5)
print(ret)
