# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return int(self.traverse(root, target, math.inf, -math.inf))

    def traverse(self, node, target, up, low):
        if node == None:
            return self.getClosest(target, up, low)
        if node.val == target:
            return target
        if node.val > target:
            return self.traverse(node.left, target, min(up, node.val), low)
        return self.traverse(node.right, target, up, max(low, node.val))

    def getClosest(self, target, up, low):
        return up if up - target < target - low else low
