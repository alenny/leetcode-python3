class Codec:

    def __init__(self):
        self.lengthLength = 10

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        for s in strs:
            ret += self.lenToChars(len(s)) + s
        return ret

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        ret = []
        i = 0
        while i < len(s):
            length = self.charsToLen(s, i)
            ret.append(s[i + self.lengthLength: i +
                         self.lengthLength + length])
            i += self.lengthLength + length
        return ret

    def lenToChars(self, length):
        s = str(length)
        for i in range(self.lengthLength - len(s)):
            s = '0' + s
        return s

    def charsToLen(self, s, begin):
        return int(s[begin:begin + self.lengthLength])

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
