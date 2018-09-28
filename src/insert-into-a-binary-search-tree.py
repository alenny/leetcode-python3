# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        self.traverse(root, val)
        return root

    def traverse(self, node, val):
        if val <= node.val:
            if node.left:
                self.traverse(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self.traverse(node.right, val)
            else:
                node.right = TreeNode(val)
