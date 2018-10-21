class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        ni, ti = 0, 0
        while ni < len(name) and ti < len(typed):
            if name[ni] != typed[ti]:
                return False
            ch = name[ni]
            bni = ni
            while ni < len(name) and name[ni] == ch:
                ni += 1
            bti = ti
            while ti < len(typed) and typed[ti] == ch:
                ti += 1
            if ti - bti < ni - bni:
                return False
        return ni == len(name) and ti == len(typed)


sol = Solution()
ret = sol.isLongPressedName("leelee", "lleeelee")
print(ret)
