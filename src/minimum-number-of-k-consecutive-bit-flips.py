from collections import deque


class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        N = len(A)
        q = deque()
        i = 0
        totalFlips = 0
        valThru = 1
        while i < N:
            while i < N and A[i] == valThru:
                i += 1
                if q and i >= q[0]:
                    q.popleft()
                    valThru = 0 if valThru == 1 else 1
            if i == N:
                break
            if N - i < K:
                return -1
            totalFlips += 1
            q.append(i + K)
            valThru = 0 if valThru == 1 else 1
        return totalFlips
