# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        total = self.getTreeSum(root)
        return self.hasSubtree(root, total >> 1)[0] if (total & 1) == 0 else False

    def getTreeSum(self, node):
        return self.getTreeSum(node.left) + node.val + self.getTreeSum(node.right) if node else 0

    def hasSubtree(self, node, targetSum):
        if node.left:
            lr = self.hasSubtree(node.left, targetSum)
            if lr[0] or lr[1] == targetSum:
                return (True, 0)
        if node.right:
            rr = self.hasSubtree(node.right, targetSum)
            if rr[0] or rr[1] == targetSum:
                return (True, 0)
        curSum = (lr[1] if node.left else 0) + \
            node.val + (rr[1] if node.right else 0)
        return (False, curSum)


# root = TreeNode(5)
# root.left = TreeNode(10)
# root.right = TreeNode(10)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(3)
# root = TreeNode(0)
# root.left = TreeNode(-1)
# root.right = TreeNode(1)
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(2)
root.left.right.left.left = TreeNode(1)
root.left.right.left.left.right = TreeNode(1)
sol = Solution()
ret = sol.checkEqualTree(root)
print(ret)
