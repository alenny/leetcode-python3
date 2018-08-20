class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        for word in words:
            if self.matchWord(word, pattern):
                ret.append(word)
        return ret

    def matchWord(self, word, pattern):
        dic = dict()
        st = set()
        for i in range(len(word)):
            key, letter = pattern[i], word[i]
            if key in dic:
                if dic[key] != letter:
                    return False
            else:
                if letter in st:
                    return False
                dic[key] = letter
                st.add(letter)
        return True
