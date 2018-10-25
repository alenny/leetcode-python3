from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, ch in enumerate(s):
            if ch in stack:
                continue
            while len(stack) > 0 and ch < stack[-1] and s.find(stack[-1], i + 1) != -1:
                stack.pop()
            if len(stack) == 0 or ch != stack[-1]:
                stack.append(ch)
        return ''.join(stack)


sol = Solution()
ret = sol.removeDuplicateLetters("cbacdcbc")
print(ret)
