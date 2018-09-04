# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math


class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.traverse(root)[0]

    def traverse(self, node):
        if not node.left and not node.right:
            return (1, node.val)
        retLeft = self.traverse(node.left) if node.left else None
        retRight = self.traverse(node.right) if node.right else None
        count = (retLeft[0] if retLeft else 0) + \
            (retRight[0] if retRight else 0)
        if not retLeft and retRight[1] == node.val or not retRight and retLeft[1] == node.val or retLeft and retRight and retLeft[1] == node.val and retRight[1] == node.val:
            return (count + 1, node.val)
        return (count, math.nan)
