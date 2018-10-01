from collections import defaultdict


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        length = len(words1)
        pairMap = defaultdict(list)
        for w0, w1 in pairs:
            pairMap[w0].append(w1)
            pairMap[w1].append(w0)
        # DFS to create tags for all unique words, using same tag for similar words
        visited = set()
        tagMap = dict()
        tag = 0
        for w in pairMap.keys():
            if w in visited:
                continue
            self.bfsTag(visited, w, pairMap, tagMap, tag)
            tag += 1
        # compare words1 and words2
        for i in range(length):
            if words1[i] != words2[i] and \
                    (not words1[i] in tagMap or
                     not words2[i] in tagMap or
                     tagMap[words1[i]] != tagMap[words2[i]]):
                return False
        return True

    def bfsTag(self, visited, word, pairMap, tagMap, tag):
        visited.add(word)
        q = [word]
        while len(q) > 0:
            nq = []
            for w in q:
                tagMap[w] = tag
                for w1 in pairMap[w]:
                    if w1 in visited:
                        continue
                    visited.add(w1)
                    nq.append(w1)
            q = nq
