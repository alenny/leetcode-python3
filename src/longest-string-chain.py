from collections import defaultdict
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPre(x, y):
            nx, ny = len(x), len(y)
            i, j = 0, 0
            while i < nx and j < ny:
                if x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == nx 

        ws = [[] for i in range(17)]
        for wi, w in enumerate(words):
            ws[len(w)].append(wi)

        graph = defaultdict(list)
        for i in range(1, 16):
            for xi in ws[i]:
                for yi in ws[i + 1]:
                    if isPre(words[xi], words[yi]):
                        graph[xi].append(yi)
        
        lengthMap = dict()

        def dfs(x):
            if x in lengthMap:
                return lengthMap[x]
            longest = 0
            for y in graph[x]:
                longest = max(longest, dfs(y))
            lengthMap[x] = longest + 1
            return lengthMap[x]
        
        for i in range(len(words)):
            dfs(i)
        return max(lengthMap.values())

sol = Solution()
ret = sol.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
print(ret)