class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        l = 0
        while l < len(str):
            r = l
            while r < len(str) and str[r] != ' ':
                r += 1
            nl = r + 1
            r -= 1
            while l < r:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1
            l = nl
