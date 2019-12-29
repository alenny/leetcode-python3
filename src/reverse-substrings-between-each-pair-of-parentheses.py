class Solution:
    def reverseParentheses(self, s: str) -> str:

        def isChar(ch):
            return ch != '(' and ch != ')'

        i = 0
        stack = ['']
        N = len(s)
        while i < N:
            if isChar(s[i]):
                stack[-1] += s[i]
            elif s[i] == '(':
                stack.append('')
            else:
                rs0 = stack.pop()[::-1]
                stack[-1] += rs0
            i += 1
        return stack[-1]


sol = Solution()
ret = sol.reverseParentheses("a(bcdefghijkl(mno)p)q")
print(ret)
