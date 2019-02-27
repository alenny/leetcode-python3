# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.__traverse(root, 0)[1]

    def __traverse(self, node, depth):
        if not node:
            return -1, None
        leftDep, leftNode = self.__traverse(node.left, depth + 1)
        rightDep, rightNode = self.__traverse(node.right, depth + 1)
        if leftDep == -1 and rightDep == -1:
            return depth, node
        if leftDep == -1 or rightDep != -1 and rightDep > leftDep:
            return rightDep, rightNode
        if rightDep == -1 or leftDep != -1 and leftDep > rightDep:
            return leftDep, leftNode
        # leftDep == rightDep
        return leftDep, node
