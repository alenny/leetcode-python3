class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.__cs = compressedString
        self.__csi = 0
        self.__currLetter = ''
        self.__currCount = 0
        self.__parseOneLetter()

    def next(self):
        """
        :rtype: str
        """
        ret = self.__currLetter if self.__currCount > 0 else ' '
        self.__currCount -= 1
        if self.__currCount == 0:
            self.__parseOneLetter()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.__currCount > 0 else False

    def __parseOneLetter(self):
        cs, csi = self.__cs, self.__csi
        if csi >= len(cs):
            self.__currCount = 0
            return
        self.__currLetter = cs[csi]
        csi += 1
        countBegin = csi
        while csi < len(cs) and cs[csi] >= '0' and cs[csi] <= '9':
            csi += 1
        self.__currCount = int(cs[countBegin:csi])
        self.__csi = csi


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
