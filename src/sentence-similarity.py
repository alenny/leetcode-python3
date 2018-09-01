from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        pairDict = defaultdict(set)
        for pair in pairs:
            pairDict[pair[0]].add(pair[1])
            pairDict[pair[1]].add(pair[0])
        for i in range(len(words1)):
            if words1[i] != words2[i] and (not words1[i] in pairDict or not words2[i] in pairDict[words1[i]]):
                return False
        return True
