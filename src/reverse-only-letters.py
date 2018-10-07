class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        countQ = []
        symbolQ = []
        letterStack = []
        count = 0
        for ch in S:
            if self.isLetter(ch):
                letterStack.append(ch)
                count += 1
            else:
                countQ.append(count)
                symbolQ.append(ch)
                count = 0
        qi = 0
        retArr = []
        while qi < len(countQ):
            for i in range(countQ[qi]):
                retArr.append(letterStack.pop())
            retArr.append(symbolQ[qi])
            qi += 1
        while len(letterStack) > 0:
            retArr.append(letterStack.pop())
        return ''.join(retArr)

    def isLetter(self, s):
        return s >= 'a' and s <= 'z' or s >= 'A' and s <= 'Z'


sol = Solution()
ret = sol.reverseOnlyLetters("Test1ng-Leet=code-Q!")
print(ret)
