from collections import defaultdict


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        posMap = [[] for _ in range(26)]
        aOrd = ord('a')
        for i, ch in enumerate(S):
            posMap(ord(ch) - aOrd).append(i)
        N = len(S)
        dp = [[(0, -1)] * 26 for _ in range(N + 1)]
        total = 0
        for c in range(26):
            if not posMap[c]:
                continue
            dp[1][c] = (1, posMap[c][0])
            total += 1
        for r in range(2, N + 1):
            pr = r - 1
            for pc in range(26):
                pCount, pEnd = dp[pr][pc]
                if pCount == 0:
                    continue
                for c in range(26):
                    ci, indexes == 0, posMap[c]
                    while indexes and ci < len(indexes) and indexes[ci] <= pEnd:
                        ci += 1
                    if not indexes or ci >= len(indexes):
                        continue
                    

        return total % (10**9 + 7)
