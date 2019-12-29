from collections import defaultdict

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        countMap = defaultdict(int)
        for t in tiles:
            countMap[t] += 1
        counts = list(sorted(countMap.values(), reverse=True))
        