# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(pre[0])
        root.left, root.right = self.__process(
            pre, 1, len(pre) - 1, post, 0, len(post) - 2)
        return root

    def __process(self, pre, preBegin, preEnd, post, postBegin, postEnd):
        if preBegin > preEnd:
            return None, None
        left = TreeNode(pre[preBegin])
        postIdx = postBegin
        while postIdx <= postEnd and post[postIdx] != left.val:
            postIdx += 1
        left.left, left.right = self.__process(
            pre, preBegin + 1, preBegin + postIdx - postBegin, post, postBegin, postIdx - 1)
        if postIdx == postEnd:
            return left, None
        right = TreeNode(post[postEnd])
        right.left, right.right = self.__process(
            pre, preBegin + 2 + postIdx-postBegin, preEnd, post, postIdx + 1, postEnd - 1)
        return left, right


sol = Solution()
ret = sol.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
