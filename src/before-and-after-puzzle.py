from collections import defaultdict
from typing import List

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        cnt = len(phrases)
        firstMap = defaultdict(list)
        lastWords = [''] * cnt
        for pi, p in enumerate(phrases):
            parts = p.split(' ')
            firstMap[parts[0]].append((pi, p))
            lastWords[pi] = parts[len(parts) - 1]
        retSet = set()
        for pi, p in enumerate(phrases):
            lw = lastWords[pi]
            for qi, q in firstMap[lw]:
                if qi == pi:
                    continue
                retSet.add(p + q[len(lw):])
        return list(sorted(retSet))

sol = Solution()
ret = sol.beforeAndAfterPuzzles(["writing code","code rocks"])        
print(ret)