# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        return self.__getNode(self.__helper(quadTree1, quadTree2))

    def __helper(self, qt1, qt2):
        if qt1.isLeaf and qt2.isLeaf:
            return qt1.val or qt2.val
        tl = self.__helper(qt1.topLeft if qt1.topLeft else qt1,
                           qt2.topLeft if qt2.topLeft else qt2)
        tr = self.__helper(qt1.topRight if qt1.topRight else qt1,
                           qt2.topRight if qt2.topRight else qt2)
        bl = self.__helper(qt1.bottomLeft if qt1.bottomLeft else qt1,
                           qt2.bottomLeft if qt2.bottomLeft else qt2)
        br = self.__helper(qt1.bottomRight if qt1.bottomRight else qt1,
                           qt2.bottomRight if qt2.bottomRight else qt2)
        return tl if tl == tr and tr == bl and bl == br else Node(False, False,
                                                                  self.__getNode(tl), self.__getNode(tr), self.__getNode(bl), self.__getNode(br))

    def __getNode(self, result):
        return result if isinstance(result, Node) else Node(result, True, None, None, None, None)
