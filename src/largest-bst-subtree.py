# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math


class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        self.traverse(root, longest)
        return longest[0]

    def traverse(self, node, longest):
        if not node:
            return 0, 0, 0
        leftBstLen, leftMin, leftMax = self.traverse(node.left, longest)
        rightBstLen, rightMin, rightMax = self.traverse(node.right, longest)
        if leftBstLen == -1 or rightBstLen == -1 or (leftBstLen > 0 and node.val <= leftMax) or (rightBstLen > 0 and node.val >= rightMin):
            return -1, 0, 0
        currBstLen = leftBstLen + rightBstLen + 1
        longest[0] = max(longest[0], currBstLen)
        return currBstLen, leftMin if leftBstLen > 0 else node.val, rightMax if rightBstLen > 0 else node.val


sol = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
ret = sol.largestBSTSubtree(root)
print(ret)
