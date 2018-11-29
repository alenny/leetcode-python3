# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum = [0]
        self.traverse(root, L, R, sum)
        return sum[0]

    def traverse(self, node, L, R, sum):
        if not node:
            return
        if node.val >= L:
            self.traverse(node.left, L, R, sum)
        if L <= node.val <= R:
            sum[0] += node.val
        if node.val <= R:
            self.traverse(node.right, L, R, sum)
