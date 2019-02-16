from collections import defaultdict


class Solution:

    def countTriplets(self, A: 'List[int]') -> 'int':
        twoMap = defaultdict(int)
        for i, a in enumerate(A):
            twoMap[a & a] += 1
            for b in A[i + 1:]:
                twoMap[a & b] += 2
        ret = 0
        for a in A:
            for two, count in twoMap.items():
                if a & two == 0:
                    ret += count
        return ret
