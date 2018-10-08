from collections import defaultdict


class Node:
    def __init__(self):
        self.wordIndexes = []
        self.children = dict()


class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        ret = ['' for i in range(len(dict))]
        abbrToWordsMap = defaultdict(list)
        for i, w in enumerate(dict):
            if len(w) < 4:
                ret[i] = w
            else:
                key = '{0}{1}{2}'.format(w[0], len(w) - 2, w[-1])
                abbrToWordsMap[key].append(i)
        for key, indexes in abbrToWordsMap.items():
            if len(indexes) == 1:
                ret[indexes[0]] = key
            else:
                self.helper(dict, indexes, ret)
        return ret

    def helper(self, dict, indexes, ret):
        root = Node()
        for idx in indexes:
            node = root
            word = dict[idx]
            for ch in word:
                node.wordIndexes.append(idx)
                if not ch in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
            node.wordIndexes.append(idx)
        q = [root]
        prefixLen = 1
        while len(q) > 0:
            nq = []
            for node in q:
                for nxt in node.children.values():
                    if len(nxt.wordIndexes) > 1:
                        nq.append(nxt)
                        continue
                    # only one word in this subtree
                    wi = nxt.wordIndexes[0]
                    w = dict[wi]
                    ret[wi] = w if len(w) - prefixLen < 3 else \
                        '{0}{1}{2}'.format(w[:prefixLen],
                                           len(w) - prefixLen - 1,
                                           w[-1])
            q = nq
            prefixLen += 1

    def getAbbr(self, word, prefixLen):
        abbr = word[:prefixLen] + str(len(word) - prefixLen - 1) + word[-1]
        return abbr if len(abbr) < len(word) else word


sol = Solution()
# ret = sol.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])
ret = sol.wordsAbbreviation(["abcdefg", "abccefg", "abcckkg"])
print(ret)
