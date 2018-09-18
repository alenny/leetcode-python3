# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.traverse(root, ret)
        return ret

    def traverse(self, node, ret):
        if not node:
            return 0
        lh = self.traverse(node.left, ret)
        rh = self.traverse(node.right, ret)
        h = max(lh, rh)
        if len(ret) <= h:
            ret.append([])
        ret[h].append(node.val)
        return h + 1
