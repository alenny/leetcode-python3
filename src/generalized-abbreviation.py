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
            abbrWordParts = []
            consecutiveAbbr = 0
            for pos in range(len(word)):
                if abbrChars & (1 << pos):
                    # abbr the char word[pos]
                    consecutiveAbbr += 1
                else:
                    # not to abbr the char word[pos]
                    if consecutiveAbbr > 0:
                        abbrWordParts.append(str(consecutiveAbbr))
                        consecutiveAbbr = 0
                    abbrWordParts.append(word[pos])
            if consecutiveAbbr > 0:
                abbrWordParts.append(str(consecutiveAbbr))
            ret.append(''.join(abbrWordParts))
        return ret


class SolutionByBackTracking:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = []
        self.helper(word, 0, [], ret)
        return ret

    def helper(self, word, idx, prefix, ret):
        if idx == len(word):
            ret.append(''.join(map(str, prefix)))
            return
        # not to abbreviate this character
        prefix.append(word[idx])
        self.helper(word, idx + 1, prefix, ret)
        prefix.pop()
        # to abbreviate this character
        if len(prefix) > 0 and isinstance(prefix[-1], int):
            prefix[-1] += 1
            self.helper(word, idx + 1, prefix, ret)
            prefix[-1] -= 1
        else:
            prefix.append(1)
            self.helper(word, idx + 1, prefix, ret)
            prefix.pop()


sol = Solution()
ret = sol.generateAbbreviations('word')
print(ret)
