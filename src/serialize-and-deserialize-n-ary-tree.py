"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        q = [root]
        data = []
        while len(q) > 0:
            nq = []
            for node in q:
                data.append('{0}:{1}'.format(node.val, len(node.children)))
                for child in node.children:
                    nq.append(child)
            q = nq
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        parts = data.split(',')
        rootVal, rootChildrenCount = [int(s) for s in parts[0].split(':')]
        root = Node(rootVal, [])
        if rootChildrenCount == 0:
            return root
        i = 1
        q = [(root, rootChildrenCount)]
        while len(q) > 0:
            nq = []
            for parent, childrenCount in q:
                for j in range(childrenCount):
                    childVal, subCount = [int(s) for s in parts[i].split(':')]
                    child = Node(childVal, [])
                    parent.children.append(child)
                    if subCount > 0:
                        nq.append((child, subCount))
                    i += 1
            q = nq
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
