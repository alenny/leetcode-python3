# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        results = []
        if not root.val in to_delete:
            results.append(root)
        delSet = set(to_delete)

        def traverse(node):
            if not node:
                return True
            leftDeleted = traverse(node.left)
            rightDeleted = traverse(node.right)
            if node.val in delSet:
                if not leftDeleted:
                    results.append(node.left)
                if not rightDeleted:
                    results.append(node.right)
                return True
            if leftDeleted:
                node.left = None
            if rightDeleted:
                node.right = None
            return False

        traverse(root)
        return results
