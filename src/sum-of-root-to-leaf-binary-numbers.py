# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Status:
    def __init__(self):
        self.path = []
        self.sum = 0


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        status = Status()
        self._traverse(root, status)
        return status.sum % (10**9 + 7)

    def _traverse(self, node, status):
        if not node:
            return
        status.path.append(str(node.val))
        if not node.left and not node.right:
            status.sum += int(''.join(status.path), 2)
        else:
            if node.left:
                self._traverse(node.left, status)
            if node.right:
                self._traverse(node.right, status)
        status.path.pop()
