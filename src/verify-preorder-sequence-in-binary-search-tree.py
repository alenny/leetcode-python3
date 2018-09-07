import math


class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # O(N) time, O(1) space
        # use the input array as the stack
        top = -1
        i = 0
        mini = -math.inf
        for i in range(len(preorder)):
            n = preorder[i]
            if n < mini:
                return False
            if top == -1 or n < preorder[top]:
                top += 1
                preorder[top] = n
            else:
                while top >= 0 and n > preorder[top]:
                    mini = preorder[top]
                    top -= 1
                top += 1
                preorder[top] = n
        return True

    def verifyPreorder1(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # O(N) time, O(logN) space
        stack = []
        mini = -math.inf
        for n in preorder:
            if n < mini:
                return False
            if len(stack) == 0 or n < stack[-1]:
                stack.append(n)
            else:
                while len(stack) > 0 and n > stack[-1]:
                    mini = stack.pop()
                stack.append(n)
        return True

    def verifyPreorderNLogN(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # O(NlogN) time, O(1) space
        inOrder = True
        if len(preorder) > 1:
            direction = preorder[1] - preorder[0]
            for i in range(1, len(preorder)):
                if direction < 0 and preorder[i] - preorder[i - 1] > 0 or direction > 0 and preorder[i] - preorder[i - 1] < 0:
                    inOrder = False
                    break
        if inOrder:
            return True
        return self.verify(preorder, 0, len(preorder) - 1, -math.inf)

    def verify(self, preorder, begin, end, mini):
        if begin > end:
            return True
        if preorder[begin] < mini:
            return False
        if begin == end:
            return True
        i = begin + 1
        while i <= end and preorder[i] < preorder[begin]:
            i += 1
        return self.verify(preorder, begin + 1, i - 1, mini) and self.verify(preorder, i, end, preorder[begin])


sol = Solution()
ret = sol.verifyPreorder([5, 2, 6, 1, 3])
