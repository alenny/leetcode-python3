class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        ai, wi = 0, 0
        while wi < len(word) and ai < len(abbr):
            while wi < len(word) and ai < len(abbr) and word[wi] == abbr[ai]:
                wi += 1
                ai += 1
            if wi >= len(word) or ai >= len(abbr):
                break
            if abbr[ai] <= '0' or abbr[ai] > '9':
                return False
            digitBegin = ai
            ai += 1
            while ai < len(abbr) and abbr[ai] >= '0' and abbr[ai] <= '9':
                ai += 1
            wi += int(abbr[digitBegin:ai])
        return wi == len(word) and ai == len(abbr)
