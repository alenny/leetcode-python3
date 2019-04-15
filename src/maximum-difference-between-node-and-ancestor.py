# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def traverse(node):
            cmin, cmax, cmaxdiff = node.val, node.val, 0
            if node.left:
                lmin, lmax, lmaxdiff = traverse(node.left)
                cmin = min(lmin, cmin)
                cmax = max(lmax, cmax)
                cmaxdiff = max(lmaxdiff, cmaxdiff, abs(
                    node.val - lmin), abs(node.val-lmax))
            if node.right:
                rmin, rmax, rmaxdiff = traverse(node.right)
                cmin = min(rmin, cmin)
                cmax = max(rmax, cmax)
                cmaxdiff = max(rmaxdiff, cmaxdiff, abs(
                    node.val - rmin), abs(node.val - rmax))
            return cmin, cmax, cmaxdiff
        return traverse(root)[2]


sol = Solution()
root = TreeNode(2)
root.left = TreeNode(5)
root.right = TreeNode(0)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(6)
root.right.left.right.left = TreeNode(1)
root.right.left.right.left.left = TreeNode(3)
ret = sol.maxAncestorDiff(root)
print(ret)
