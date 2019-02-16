import math


class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sInt, sNr, sr = self.getParts(S)
        tInt, tNr, tr = self.getParts(T)
        if (sInt, sNr, sr) == (tInt, tNr, tr):
            return True
        if sInt != tInt or sr and not tr or not sr and tr or not sr and not tr:
            return False
        sl = len(sNr) + len(sr) * 2
        tl = len(tNr) + len(tr) * 2
        return self.compare(sNr, sr, tNr, tr) if sl < tl else self.compare(tNr, tr, sNr, sr)

    def compare(self, shortNr, shortR, longNr, longR):
        longX = longNr + longR * 2
        shortRepeat = math.ceil((len(longX) - len(shortNr)) / len(shortR))
        shortX = shortNr + shortR * shortRepeat
        return shortX.startswith(longX)

    def getParts(self, N):
        parts = N.split('.')
        intPart = parts[0]
        if len(parts) == 1:
            return intPart, '', ''
        leftPara = parts[1].find('(')
        if leftPara < 0:
            return intPart, parts[1], ''
        nonRepeatPart = parts[1][:leftPara]
        repeatPart = parts[1][leftPara + 1:len(parts[1]) - 1]
        if repeatPart == '9' * len(repeatPart):
            if not nonRepeatPart:
                intPart = str(int(intPart) + 1)
            else:
                plusOneStr = str(int(nonRepeatPart) + 1)
                if len(plusOneStr) > len(nonRepeatPart):
                    intPart = str(int(intPart) + 1)
                    nonRepeatPart = ''
                else:
                    nonRepeatPart = plusOneStr.zfill(len(nonRepeatPart))
            repeatPart = ''
        elif repeatPart == '0' * len(repeatPart):
            repeatPart = ''
        return intPart, nonRepeatPart, repeatPart


sol = Solution()
ret = sol.isRationalEqual("0.08(9)", "0.09")
print(ret)
