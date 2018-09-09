# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if (N & 1) == 0:
            return []
        matrix = [[] for i in range(20)]
        matrix[1].append(TreeNode(0))
        for n in range(3, N + 1, 2):
            for lCount in range(1, n - 1, 2):
                rCount = n - 1 - lCount
                for lPart in matrix[lCount]:
                    for rPart in matrix[rCount]:
                        root = TreeNode(0)
                        root.left = lPart
                        root.right = rPart
                        matrix[n].append(root)
        return matrix[N]


sol = Solution()
ret = sol.allPossibleFBT(19)
