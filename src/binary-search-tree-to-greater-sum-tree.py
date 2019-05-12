# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def traverse(node, prevSum):
            if not node:
                return prevSum
            node.val = node.val + \
                (traverse(node.right, prevSum) if node.right else prevSum)
            maxVal = traverse(node.left, node.val)
            return maxVal

        traverse(root, 0)
        return root


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
sol = Solution()
ret = sol.bstToGst(root)
print(ret)
