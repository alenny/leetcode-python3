from collections import defaultdict


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idxMap = defaultdict(list)
        for i in range(len(words)):
            idxMap[words[i]].append(i)
        i1List, i2List = idxMap[word1], idxMap[word2]
        shortest = len(words)
        for i1 in i1List:
            for i2 in i2List:
                shortest = min(shortest, abs(i1 - i2))
        return shortest
