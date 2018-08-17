class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        wd = dict()
        self.processWords(wd, A)
        self.processWords(wd, B)
        ret = []
        for k, v in wd.items():
            if v == 1:
                ret.append(k)
        return ret

    def processWords(self, wd, sentence):
        wl = sentence.split()
        for w in wl:
            if w in wd:
                wd[w] = wd[w] + 1
            else:
                wd[w] = 1


sol = Solution()
sol.uncommonFromSentences("this apple is sweet", "this apple is sour")
