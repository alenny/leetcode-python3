class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        idxMap = dict()
        for idx, word in enumerate(words):
            idxMap[word] = idx
        ret = []
        emptyIdx = idxMap[''] if '' in idxMap else -1
        for idx, word in enumerate(words):
            rw = word[::-1]
            if rw > word and rw in idxMap:
                rwIdx = idxMap[rw]
                ret.append([idx, rwIdx])
                ret.append([rwIdx, idx])
            if word and emptyIdx != -1 and self.isPalindrome(word, 0, len(word) - 1):
                ret.append([emptyIdx, idx])
                ret.append([idx, emptyIdx])
            for ri in range(len(word) - 1):
                if not self.isPalindrome(word, 0, ri):
                    continue
                target = word[ri + 1:][::-1]
                if target in idxMap:
                    ret.append([idxMap[target], idx])
            for li in range(1, len(word)):
                if not self.isPalindrome(word, li, len(word) - 1):
                    continue
                target = word[:li][::-1]
                if target in idxMap:
                    ret.append([idx, idxMap[target]])
        return ret

    def isPalindrome(self, s, li, ri):
        halfLen = ri - li + 1 >> 1
        left = s[li:li + halfLen]
        return s.endswith(left[::-1], li, ri + 1)
