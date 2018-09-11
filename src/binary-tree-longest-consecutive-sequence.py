# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import math


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, math.nan, 0)

    def traverse(self, node, parentVal, parentConsecutiveLength):
        if not node:
            return parentConsecutiveLength
        currLen = parentConsecutiveLength + 1 if node.val == parentVal + 1 else 1
        left = self.traverse(node.left, node.val, currLen)
        right = self.traverse(node.right, node.val, currLen)
        return max(parentConsecutiveLength, left, right)


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
ret = sol.longestConsecutive(root)
print(ret)
