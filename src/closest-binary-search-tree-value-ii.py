# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        arr = []
        ci = self.traverse(root, target, arr)
        l, r = (ci - 1, ci) if ci >= 0 else (len(arr) - 1, len(arr))
        ret = []
        while (l >= 0 or r < len(arr)) and k > 0:
            if l < 0:
                ret.append(arr[r])
                r += 1
            elif r >= len(arr):
                ret.append(arr[l])
                l -= 1
            elif arr[r] - target <= target - arr[l]:
                ret.append(arr[r])
                r += 1
            else:
                ret.append(arr[l])
                l -= 1
            k -= 1
        return ret

    def traverse(self, node, target, arr):
        if not node:
            return -1
        ret = self.traverse(node.left, target, arr)
        if ret == -1 and node.val >= target:
            ret = len(arr)
        arr.append(node.val)
        rr = self.traverse(node.right, target, arr)
        return ret if ret != -1 else rr
