# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if val > root.val:
            newNode.left = root
            return newNode
        self.insertHelper(root.right, root, newNode)
        return root

    def insertHelper(self, node, parent, newNode):
        if not node:
            parent.right = newNode
            return
        if newNode.val > node.val:
            parent.right = newNode
            newNode.left = node
            return
        self.insertHelper(node.right, node, newNode)
