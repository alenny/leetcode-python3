# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def traverse(vals, depths, left, right):
            root = TreeNode(vals[left])
            if right == left:
                return root
            i = left + 2
            while i <= right:
                if depths[i] == depths[left + 1]:
                    break
                i += 1
            root.left = traverse(vals, depths, left + 1, i - 1)
            if i <= right:
                root.right = traverse(vals, depths, i, right)
            return root

        if not S:
            return None
        vals = []
        depths = []
        i = 0
        N = len(S)
        while i < N:
            b = i
            while i < N and S[i] == '-':
                i += 1
            depth = i - b
            b = i
            while i < N and S[i] != '-':
                i += 1
            val = int(S[b:i])
            vals.append(val)
            depths.append(depth)
        return traverse(vals, depths, 0, len(vals) - 1)
