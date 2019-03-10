# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = list(sorted(preorder))
        return self.construct(preorder, inorder)

    def construct(self, preorder, inorder):
        N = len(preorder)
        if N == 0:
            return None
        node = TreeNode(preorder[0])
        if N == 1:
            return node
        idx = self.binarySearch(inorder, preorder[0], 0, N - 1)
        node.left = self.construct(preorder[1:idx + 1], inorder[:idx])
        node.right = self.construct(preorder[idx + 1:], inorder[idx + 1:])
        return node

    def binarySearch(self, arr, target, b, e):
        if b > e:
            return None
        mid = b + e >> 1
        if arr[mid] == target:
            return mid
        return self.binarySearch(arr, target, b, mid - 1) if arr[mid] > target \
            else self.binarySearch(arr, target, mid + 1, e)
