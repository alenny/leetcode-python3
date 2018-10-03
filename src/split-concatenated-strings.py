class Solution:
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ss = [max(s, s[::-1]) for s in strs]
        maxS = ''
        for i, s in enumerate(ss):
            left = ''.join(ss[:i])
            right = ''.join(ss[i + 1:])
            for j in range(len(s)):
                maxS = max(maxS, s[j:] + right + left + s[:j])
            rs = s[::-1]
            for j in range(len(rs)):
                maxS = max(maxS, rs[j:] + right + left + rs[:j])
        return maxS


sol = Solution()
ret = sol.splitLoopedString(['abc', 'xyz'])
print(ret)
