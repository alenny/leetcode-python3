# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        # returns (maxAvg, sum, nodeCount)
        def traverse(node):
            if not node:
                return 0, 0, 0
            leftMaxAvg, leftSum, leftNodeCount = traverse(node.left)
            rightMaxAvg, rightSum, rightNodeCount = traverse(node.right)
            curNodeCount = leftNodeCount + rightNodeCount + 1
            curSum = leftSum + rightSum + node.val
            return max(curSum / curNodeCount, leftMaxAvg, rightMaxAvg), curSum, curNodeCount

        return traverse(root)[0]