class Node:
    def __init__(self):
        self.word = ''
        self.children = dict()


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = Node()
        for word in words:
            node = root
            for ch in word:
                if not ch in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
            node.word = word
        ret = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.bfs(board, r, c, root, ret)
        return list(ret)

    def bfs(self, board, r, c, root, ret):
        rows, cols = len(board), len(board[0])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(r, c, set([self.getKey(r, c)]), root)]
        while len(q) > 0:
            nq = []
            for r0, c0, pathSet, node in q:
                ch = board[r0][c0]
                if not ch in node.children:
                    continue
                curNode = node.children[ch]
                if curNode.word:
                    ret.add(curNode.word)
                for dr, dc in deltas:
                    r1, c1 = r0 + dr, c0 + dc
                    key = self.getKey(r1, c1)
                    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or key in pathSet:
                        continue
                    newPathSet = pathSet.copy()
                    newPathSet.add(key)
                    nq.append((r1, c1, newPathSet, curNode))
            q = nq

    def getKey(self, r, c):
        return '{0},{1}'.format(r, c)


sol = Solution()
ret = sol.findWords([["a", "b"], ["a", "a"]], [
                    "aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"])
# ret = sol.findWords([
#     ['o', 'a', 'a', 'n'],
#     ['e', 't', 'a', 'e'],
#     ['i', 'h', 'k', 'r'],
#     ['i', 'f', 'l', 'v']
# ], ["oath", "pea", "eat", "rain"])
