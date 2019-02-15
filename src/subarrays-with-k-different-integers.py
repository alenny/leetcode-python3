from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        return self.subarraysWithKDistinctByAtMost(A, K)

    def subarraysWithKDistinctByAtMost(self, A: 'List[int]', K: 'int') -> 'int':
        return self.countAtMostK(A, K) - self.countAtMostK(A, K - 1)

    def countAtMostK(self, A, K):
        if K == 0:
            return 0
        N = len(A)
        countMap = defaultdict(int)
        ret, l, r = 0, 0, 0
        while l < N:
            while r < N and (len(countMap) < K or len(countMap) == K and A[r] in countMap):
                countMap[A[r]] += 1
                r += 1
            ret += r - l
            countMap[A[l]] -= 1
            if countMap[A[l]] == 0:
                countMap.pop(A[l])
            l += 1
        return ret

    def subarraysWithKDistinctWithBackSearch(self, A: 'List[int]', K: 'int') -> 'int':
        N = len(A)
        countMap = defaultdict(int)
        ret = 0
        l, r = 0, 0
        while r < N:
            countMap[A[r]] += 1
            if len(countMap) < K:
                r += 1
                continue
            if len(countMap) == K:
                ret += 1
                r += 1
                continue
            countMap[A[l]] -= 1
            if countMap[A[l]] == 0:
                countMap.pop(A[l])
            l += 1
            ret += self.backSearch(A, countMap, K, l, r)
            r += 1
        while l < N and len(countMap) >= K:
            countMap[A[l]] -= 1
            if countMap[A[l]] == 0:
                countMap.pop(A[l])
            l += 1
            ret += self.backSearch(A, countMap, K, l, N - 1)
        return ret

    def backSearch(self, A, countMap, K, left, right):
        tempMap = dict()
        rr = right
        ret = 0
        while rr >= left and len(countMap) >= K:
            if len(countMap) == K:
                ret += 1
            if rr == left:
                break
            if not A[rr] in tempMap:
                tempMap[A[rr]] = countMap[A[rr]]
            countMap[A[rr]] -= 1
            if countMap[A[rr]] == 0:
                countMap.pop(A[rr])
            rr -= 1
        for k, v in tempMap.items():
            countMap[k] = v
        return ret


sol = Solution()
ret = sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
print(ret)
