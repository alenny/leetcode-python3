class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        i = 0
        while i < len(s) - 1:
            while i < len(s) - 1 and s[i] != '+':
                i += 1
            if i >= len(s) - 1:
                break
            if s[i + 1] == '+':
                ret.append(self.replace(s, i))
            i += 1
        return ret

    def replace(self, s, i):
        return s[:i] + '--' + s[i + 2:]
