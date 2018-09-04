from collections import defaultdict
import heapq


class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.list = []


class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TreeNode()
        self.times = defaultdict(int)
        self.currSentence = ''
        self.currNode = self.root
        self.top = 3
        for i in range(len(sentences)):
            self.commitSentence(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.commitSentence(self.currSentence, 0)
            self.currSentence = ''
            self.currNode = self.root
            return []
        self.currSentence += c
        return self.findTopSentences(c)

    def findTopSentences(self, letter):
        self.currNode = self.currNode.children[letter]
        # use nsmallest because the secondary sorting factor is the sentence itself
        return heapq.nsmallest(3, self.currNode.list, key=lambda s: (self.times[s], s))

    def commitSentence(self, sentence, time):
        # time == 0 means increase time by 1 (-1)
        newSentence = not sentence in self.times
        if time == 0:
            self.times[sentence] -= 1
        else:
            self.times[sentence] = -time
        node = self.root
        i = 0
        while i < len(sentence):
            letter = sentence[i]
            node = node.children[letter]
            if newSentence:
                node.list.append(sentence)
            i += 1


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

sys = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
ret = sys.input("i")
ret = sys.input(" ")
ret = sys.input("a")
ret = sys.input("#")
ret = sys.input("i")
ret = sys.input(" ")
ret = sys.input("a")
ret = sys.input("#")
ret = sys.input("i")
ret = sys.input(" ")
ret = sys.input("a")
ret = sys.input("#")
