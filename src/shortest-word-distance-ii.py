from collections import defaultdict


class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.total = len(words)
        self.map = defaultdict(list)
        for i in range(self.total):
            self.map[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.map[word1]
        l2 = self.map[word2]
        minDist = self.total
        i1, i2 = 0, 0
        while i1 < len(l1) and i2 < len(l2):
            minDist = min(minDist, abs(l1[i1]-l2[i2]))
            if minDist == 1:
                break
            if (l1[i1] < l2[i2]):
                i1 += 1
            else:
                i2 += 1
        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
