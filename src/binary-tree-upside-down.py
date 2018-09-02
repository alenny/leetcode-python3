# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        newRoot = self.traverse(root, None)
        if root:
            root.right = None
        return newRoot

    def traverse(self, node, rightSib):
        if not node:
            return None
        newRoot = self.traverse(node.left, node.right)
        if node.left:
            node.left.right = node
        node.left = rightSib
        return newRoot if newRoot else node
