class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # every character has two status: abbr(1) or not abbr(0).
        # so we use binary to represent the status of the whole word.
        # so the total abbr count is pow(2, len(word))
        ret = []
        total = pow(2, len(word))
        for abbrChars in range(total):
            abbrWord = ''
            consecutiveAbbr = 0
            for pos in range(len(word)):
                if abbrChars & (1 << pos):
                    # abbr the char word[pos]
                    consecutiveAbbr += 1
                else:
                    # not to abbr the char word[pos]
                    if consecutiveAbbr > 0:
                        abbrWord += str(consecutiveAbbr)
                        consecutiveAbbr = 0
                    abbrWord += word[pos]
            if consecutiveAbbr > 0:
                abbrWord += str(consecutiveAbbr)
            ret.append(abbrWord)
        return ret
