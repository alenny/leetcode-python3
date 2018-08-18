class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        K -= 1
        stack, si, cs = [], 0, ""
        while si < len(S):
            if S[si] < "0" or S[si] > "9":
                cs += S[si]
                si += 1
                continue
            if len(stack) > 0:
                prevLen = stack[-1][1]
            else:
                prevLen = 0
            if cs != "":
                stack.append(cs)
            newRepeat = int(S[si])
            newLen = (prevLen + len(cs)) * newRepeat
            stack.append((newRepeat, newLen))
            cs = ""
            if (newLen > K):
                break
            si += 1
        if cs != "":
            stack.append(cs)
        top = ()
        while len(stack) > 0:
            top = stack.pop()
            if isinstance(top, tuple):
                K = int(K % (top[1] / top[0]))
            elif len(stack) > 0:
                if stack[-1][1] <= K:
                    return top[K - stack[-1][1]]
        return top[K]


sol = Solution()
ret = sol.decodeAtIndex("ha22", 5)
ret = sol.decodeAtIndex("a2345678999999999999999", 1)
ret = sol.decodeAtIndex("leet2code3", 10)
ret = sol.decodeAtIndex("abc", 1)
ret = sol.decodeAtIndex("a2b3c4d5e6f7g8h9", 3)
print(ret)
