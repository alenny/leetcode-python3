# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        colMap = defaultdict(list)
        self.traverse(root, colMap)
        cols = list(colMap.items())
        cols.sort(key=lambda itm: itm[0])
        ret = []
        for k, v in cols:
            ret.append(v)
        return ret

    def traverse(self, root, colMap):
        q = [(root, 0)]
        while len(q) > 0:
            nq = []
            for node, col in q:
                colMap[col].append(node.val)
                if node.left:
                    nq.append((node.left, col - 1))
                if node.right:
                    nq.append((node.right, col + 1))
            q = nq
