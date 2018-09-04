# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        self.traverse(root, inorder)
        if len(inorder) == 0:
            return None
        inorder.append(None)
        for i in range(len(inorder) - 1):
            inorder[i].left = None
            inorder[i].right = inorder[i + 1]
        return inorder[0]

    def traverse(self, node, inorder):
        if not node:
            return
        self.traverse(node.left, inorder)
        inorder.append(node)
        self.traverse(node.right, inorder)
