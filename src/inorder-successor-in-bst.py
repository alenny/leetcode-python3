# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # status: 0: p not found, 1: p found but successor not found, 2: successor found
        return self.traverse(root, p, [0])

    def traverse(self, node, p, status):
        if not node:
            return None
        if status[0] == 0:
            if node == p:
                status[0] = 1
                return self.traverse(node.right, p, status)
            ret = self.traverse(node.left, p, status)
            if status[0] == 0:
                return self.traverse(node.right, p, status)
            if status[0] == 1:
                status[0] = 2
                return node
            return ret  # status: 2
        # status: 1
        ret = self.traverse(node.left, p, status)
        status[0] = 2
        # would not be status 2 here
        return ret if ret else node
