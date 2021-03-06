"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret = []
        self.traverse(root, ret)
        return ret

    def traverse(self, node, ret):
        if not node:
            return
        for ch in node.children:
            self.traverse(ch, ret)
        ret.append(node.val)
