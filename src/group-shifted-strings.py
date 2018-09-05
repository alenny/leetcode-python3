from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dicty = defaultdict(list)
        for s in strings:
            key = str(len(s)) + ','
            for i in range(len(s) - 1):
                if s[i + 1] >= s[i]:
                    key += str(ord(s[i + 1]) - ord(s[i])) + ','
                else:
                    key += str(ord(s[i + 1]) - ord('a') +
                               1 + ord('z') - ord(s[i])) + ','
            dicty[key].append(s)
        ret = []
        for ws in dicty.values():
            ret.append(ws)
        return ret
