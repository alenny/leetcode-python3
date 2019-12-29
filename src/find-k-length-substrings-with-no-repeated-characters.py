from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        L = len(S)
        if K > L:
            return 0
        chMap = defaultdict(int)
        i = 0
        while i < K:
            chMap[S[i]] += 1
            i += 1
        ret = 1 if len(chMap) == K else 0
        while i < L:
            ri = i - K
            chMap[S[ri]] -= 1
            chMap[S[i]] += 1
            if chMap[S[ri]] == 0:
                chMap.pop(S[ri])
            if len(chMap) == K:
                ret += 1
            i += 1
        return ret