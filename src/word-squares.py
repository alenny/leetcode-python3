class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.words = []
        self.children = dict()


class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        N = len(words[0])
        root = TrieNode('')
        for word in words:
            node = root
            for ch in word:
                if not ch in node.children:
                    node.children[ch] = TrieNode(ch)
                node = node.children[ch]
                node.words.append(word)
        ret = []
        for word in words:
            self.dfs([word], root, ret)
        return ret

    def dfs(self, inWords, root, ret):
        idx = len(inWords)
        N = len(inWords[0])
        if idx == N:
            ret.append(inWords[:])
            return
        node = root
        for i in range(idx):
            ch = inWords[i][idx]
            if not ch in node.children:
                return
            node = node.children[ch]
        for w in node.words:
            inWords.append(w)
            self.dfs(inWords, root, ret)
            inWords.pop()


sol = Solution()
ret = sol.wordSquares(["area", "lead", "wall", "lady", "ball"])
print('ok')
