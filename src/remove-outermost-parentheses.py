class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if S == '':
            return S
        ret = ''
        l = 0
        N = len(S)
        while l < N:
            r = l
            lc, rc = 0, 0
            while r < N and (lc != rc or lc == 0 and rc == 0):
                if S[r] == '(':
                    lc += 1
                else:
                    rc += 1
                r += 1
            if lc == rc and lc != 0 and rc != 0:
                ret += S[l+1:r-1]
            l = r
        return ret


sol = Solution()
ret = sol.removeOuterParentheses("(()())(())")
print(ret)
ret = sol.removeOuterParentheses("(()())(())(()(()))")
print(ret)
ret = sol.removeOuterParentheses("()()")
print(ret)
ret = sol.removeOuterParentheses("()")
print(ret)
ret = sol.removeOuterParentheses("")
print(ret)
