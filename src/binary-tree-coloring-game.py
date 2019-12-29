# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def findNodeX(nd):
            if not nd:
                return None
            if nd.val == x:
                return nd
            ret = findNodeX(nd.left)
            return ret if ret else findNodeX(nd.right)

        def countNodes(rt):
            return 0 if not rt else countNodes(rt.left) + countNodes(rt.right) + 1

        nodeX = findNodeX(root)
        leftCount = countNodes(nodeX.left)
        rightCount = countNodes(nodeX.right)
        countInParent = n - leftCount - rightCount - 1
        return countInParent > leftCount + rightCount + 1 \
            or leftCount > countInParent + rightCount + 1 \
            or rightCount > countInParent + leftCount + 1
