from collections import defaultdict


class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        posMap = defaultdict(list)
        for i in range(len(words)):
            posMap[words[i]].append(i)
        l1 = posMap[word1]
        if word1 == word2:
            shortest = len(words)
            for i in range(len(l1) - 1):
                shortest = min(shortest, l1[i + 1] - l1[i])
                if shortest == 1:
                    return 1
            return shortest
        l2 = posMap[word2]
        i1, i2 = 0, 0
        shortest = len(words)
        while i1 < len(l1) and i2 < len(l2):
            shortest = min(shortest, abs(l1[i1] - l2[i2]))
            if l1[i1] > l2[i2]:
                i2 += 1
            else:
                i1 += 1
        return shortest
