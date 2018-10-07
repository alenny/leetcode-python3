# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.parentQueue = deque()
        # bfs
        q = [root]
        while len(q) > 0:
            nq = []
            for node in q:
                if not node.left or not node.right:
                    self.parentQueue.append(node)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.parentQueue[0]
        newNode = TreeNode(v)
        if not parent.left:
            parent.left = newNode
        else:
            parent.right = newNode
            self.parentQueue.popleft()
        self.parentQueue.append(newNode)
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
