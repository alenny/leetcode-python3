"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        depth = 0
        while len(q) > 0:
            depth += 1
            nq = []
            for node in q:
                nq += node.children
            q = nq
        return depth
