class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenDiff = len(s) - len(t)
        if abs(lenDiff) > 1:
            return False
        si = ti = 0
        oneStepUsed = False
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
                continue
            if oneStepUsed:
                return False
            oneStepUsed = True
            if lenDiff == 1:
                si += 1
            elif lenDiff == -1:
                ti += 1
            else:
                si += 1
                ti += 1
        return oneStepUsed or abs(lenDiff) == 1


sol = Solution()
ret = sol.isOneEditDistance('a', 'A')
