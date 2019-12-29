from collections import defaultdict

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourceMap = defaultdict(list)
        for i, ch in enumerate(source):
            sourceMap[ch].append(i)
        ret = 1
        si = -1
        SL = len(source)
        for ch in target:
            if not ch in sourceMap:
                return -1   # Unknown character
            foundPos = -1
            for pos in sourceMap[ch]:
                if pos > si:
                    foundPos = pos
                    break
            if foundPos == -1:
                ret += 1
                foundPos = sourceMap[ch][0]
            si = foundPos
        return ret