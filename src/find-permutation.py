class Solution:
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if len(s) == 0:
            return [1]
        si = 0
        ret = []
        low = 1
        while si < len(s):
            sameBegin = si
            while si < len(s) and s[si] == s[sameBegin]:
                si += 1
            if s[sameBegin] == 'I':
                high = low + si - sameBegin - \
                    (0 if sameBegin == 0 and si == len(s) else
                     (1 if sameBegin == 0 or si == len(s) else 2))
                for i in range(low, high + 1):
                    ret.append(i)
            else:
                # 'D'
                high = low + si - sameBegin
                for i in range(high, low - 1, -1):
                    ret.append(i)
            low = high + 1
        return ret


sol = Solution()
#ret = sol.findPermutation('DDIIDI')
ret = sol.findPermutation('III')
print(ret)
