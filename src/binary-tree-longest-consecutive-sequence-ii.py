# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root)[0]

    def traverse(self, node):
        # return values: [0]: longest path, [1]: longest increasing path to node
        # [2]: longest decreasing path to node
        if not node:
            return (0, 0, 0)
        leftLongest, leftIncLongest, leftDecLongest = self.traverse(node.left)
        rightLongest, rightIncLongest, rightDecLongest = self.traverse(
            node.right)
        incLongest = max(
            leftIncLongest + 1 if leftIncLongest > 0 and node.val == node.left.val + 1 else 1,
            rightIncLongest + 1 if rightIncLongest > 0 and node.val == node.right.val + 1 else 1)
        decLongest = max(
            leftDecLongest + 1 if leftDecLongest > 0 and node.val == node.left.val - 1 else 1,
            rightDecLongest + 1 if rightDecLongest > 0 and node.val == node.right.val - 1 else 1)
        longest = max(leftLongest, rightLongest, incLongest, decLongest)
        if leftIncLongest > 0 and rightDecLongest > 0 and node.val == node.left.val + 1 and node.val == node.right.val - 1:
            longest = max(longest, leftIncLongest + 1 + rightDecLongest)
        if leftDecLongest > 0 and rightIncLongest > 0 and node.val == node.left.val - 1 and node.val == node.right.val + 1:
            longest = max(longest, leftDecLongest + 1 + rightIncLongest)
        return (longest, incLongest, decLongest)
