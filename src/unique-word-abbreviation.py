from collections import defaultdict


class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = defaultdict(set)
        for w in dictionary:
            self.dic[self.getAbbr(w)].add(w)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.getAbbr(word)
        return not abbr in self.dic or word in self.dic[abbr] and len(self.dic[abbr]) == 1

    def getAbbr(self, word):
        return word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
