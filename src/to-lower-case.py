class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        aCode = ord('a')
        ACode = ord('A')
        ZCode = ord('Z')
        codeDiff = aCode - ACode
        parts = []
        for i in range(len(str)):
            code = ord(str[i])
            if code >= ACode and code <= ZCode:
                parts.append(chr(code + codeDiff))
            else:
                parts.append(str[i])
        return ''.join(parts)
