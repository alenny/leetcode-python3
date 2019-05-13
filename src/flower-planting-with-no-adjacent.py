from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        ret = [0] * (N + 1)
        joinMap = defaultdict(list)
        for x, y in paths:
            joinMap[x].append(y)
            joinMap[y].append(x)
        for first in range(1, N + 1):
            if ret[first] != 0:
                continue
            ret[first] = 1
            q = [first]
            nextFlower = 2
            while q:
                nq = []
                for cur in q:
                    for nxt in joinMap[cur]:
                        if ret[nxt] != 0 and ret[nxt] != ret[cur]:
                            continue
                        ret[nxt] = nextFlower
                        nq.append(nxt)
                nextFlower = (nextFlower) % 4 + 1
                q = nq
        return ret[1:]
