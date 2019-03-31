class Solution:
    def prefixesDivBy5(self, A):
        ret = []
        B = ''.join(map(str, A))
        for i in range(len(B)):
            s = B[:i + 1]
            x = int(s, 2)
            ret.append(x % 5 == 0)
        return ret


sol = Solution()
ret = sol.prefixesDivBy5([0, 1, 1, 1, 1, 1])
print(ret)
