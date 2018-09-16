# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        return self.traverse(root, V)

    def traverse(self, node, V):
        if not node:
            return [None, None]
        if node.val > V:
            leftSmall, node.left = self.traverse(node.left, V)
            return [leftSmall, node]
        # node.val <= V
        node.right, rightBig = self.traverse(node.right, V)
        return [node, rightBig]


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
sol = Solution()
ret = sol.splitBST(root, 2)
print('ok')
