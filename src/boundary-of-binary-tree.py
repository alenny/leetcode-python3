# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        leftBoundary = [root]
        rightBoundary = [root]
        if root.left:
            self.findLeftBoundary(root.left, leftBoundary)
        leaves = []
        self.findLeaves(root, leaves)
        if root.right:
            self.findRightBoundary(root.right, rightBoundary)
        rightBoundary.reverse()
        output = []
        outNodeSet = set()
        for node in (leftBoundary + leaves + rightBoundary):
            if node in outNodeSet:
                continue
            output.append(node.val)
            outNodeSet.add(node)
        return output

    def findLeftBoundary(self, node, leftBoundary):
        leftBoundary.append(node)
        if node.left:
            self.findLeftBoundary(node.left, leftBoundary)
        elif node.right:
            self.findLeftBoundary(node.right, leftBoundary)

    def findRightBoundary(self, node, rightBoundary):
        rightBoundary.append(node)
        if node.right:
            self.findRightBoundary(node.right, rightBoundary)
        elif node.left:
            self.findRightBoundary(node.left, rightBoundary)

    def findLeaves(self, node, leaves):
        if not node.left and not node.right:
            leaves.append(node)
            return
        if node.left:
            self.findLeaves(node.left, leaves)
        if node.right:
            self.findLeaves(node.right, leaves)
