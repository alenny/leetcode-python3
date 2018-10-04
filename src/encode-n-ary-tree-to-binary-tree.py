# """
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
# """
# """
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# """


from collections import deque


class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        stream = self.encNary(root)
        return self.decBinary(stream)

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        stream = self.encBinary(data)
        return self.decNary(stream)

    def encBinary(self, root):
        if not root:
            return ''
        ret = ''
        q = [root]
        while len(q) > 0:
            nq = []
            for node in q:
                ret += node.val + ','
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
        return ret

    def decBinary(self, stream):
        if not stream:
            return None
        parts = stream.split(',')[:-1]
        root = TreeNode(parts[0])
        nodeQ = deque([[root, 2]])
        i = 1
        for i in range(1, len(parts)):
            node = TreeNode(parts[i])
            nodeQ.append([node, 2])
            if nodeQ[0][1] == 2:
                nodeQ[0][0].left = node
                nodeQ[0][1] -= 1
            elif nodeQ[0][1] == 1:
                nodeQ[0][0].right = node
                nodeQ.popleft()
        return root

    def encNary(self, root):
        if not root:
            return ''
        q = [root]
        ret = ''
        while len(q) > 0:
            nq = []
            for node in q:
                ret += '{0}:{1},'.format(node.val, len(node.children))
                for child in node.children:
                    nq.append(child)
            q = nq
        return ret

    def decNary(self, stream):
        if not stream:
            return None
        parts = stream.split(',')[:-1]
        val, childCount = [int(p) for p in parts[0].split(':')]
        root = Node(val, [])
        nodeQ = deque([[root, childCount]])
        for i in range(1, len(parts)):
            val, childCount = [int(p) for p in parts[i].split(':')]
            node = Node(val, [])
            if childCount > 0:
                nodeQ.append([node, childCount])
            nodeQ[0][0].children.append(node)
            nodeQ[0][1] -= 1
            if nodeQ[0][1] == 0:
                nodeQ.popleft()
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))


codec = Codec()
root = Node(1, [])
root.children.append(Node(3, []))
root.children.append(Node(2, []))
root.children.append(Node(4, []))
root.children[0].children.append(Node(5, []))
root.children[0].children.append(Node(6, []))
bRoot = codec.encode(root)
root1 = codec.decode(bRoot)
print('ok')
