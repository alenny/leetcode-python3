class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        size = len(words)
        for r in range(0, size):
            if len(words[r]) > size:
                return False
            for c in range(0, r):
                if c >= len(words[r]) and r >= len(words[c]):
                    continue
                if r >= len(words[c]) or c >= len(words[r]) or words[r][c] != words[c][r]:
                    return False
        return True


sol = Solution()
ret = sol.validWordSquare(["ball", "asee", "lett", "le"])
