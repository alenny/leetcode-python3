# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        stack = []
        i = len(s) - 1
        numStr = ''
        while i >= -1:
            if i == -1 or s[i] == '(':
                newNode = TreeNode(int(numStr))
                if len(stack) > 0 and isinstance(stack[-1], TreeNode):
                    newNode.left = stack.pop()
                    if len(stack) > 0 and isinstance(stack[-1], TreeNode):
                        newNode.right = stack.pop()
                if len(stack) > 0:
                    stack.pop()     # pop ')'
                stack.append(newNode)
                numStr = ''
                i -= 1
                continue
            if s[i] == ')':
                stack.append(')')
                i -= 1
                continue
            numStr = s[i] + numStr
            i -= 1
        return stack[0]


sol = Solution()
ret = sol.str2tree("4(2(3)(1))(6(5))")
print('ok')
