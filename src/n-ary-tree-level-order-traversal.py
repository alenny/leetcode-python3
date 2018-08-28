"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        ret = []
        while len(q) > 0:
            lvl = []
            ret.append(lvl)
            nq = []
            for node in q:
                lvl.append(node.val)
                nq += node.children
            q = nq
        return ret
