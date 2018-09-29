# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


class Status:
    def __init__(self):
        self.foundLeaf = None
        self.foundDistance = math.inf
        self.distance = -1


class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        status = Status()
        self.traverse(root, k, status)
        return status.foundLeaf.val

    def traverse(self, node, k, status):
        if not node:
            return
        if node.val == k:
            if not node.left and not node.right:
                status.foundLeaf = node
                status.foundDistance = 0
            else:
                status.distance = 1
                self.traverse(node.left, k, status)
                self.traverse(node.right, k, status)
            return
        kFoundInParent = status.distance != -1
        if kFoundInParent and not node.left and not node.right and status.distance < status.foundDistance:
            status.foundLeaf = node
            status.foundDistance = status.distance
            return
        if kFoundInParent:
            status.distance += 1
        self.traverse(node.left, k, status)
        kFoundInLeft = status.distance != -1
        self.traverse(node.right, k, status)
        if kFoundInParent:
            status.distance -= 1
            return
        if not kFoundInLeft and status.distance != -1:
            self.traverse(node.left, k, status)
        if status.distance != -1:
            status.distance += 1
