from collections import defaultdict
import math


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) < 2:
            return False
        cardCounts = defaultdict(int)
        for card in deck:
            cardCounts[card] += 1
        countList = list(cardCounts.values())
        countList.sort()
        prevNum = countList[0]
        if prevNum < 2:
            return False
        for i in range(1, len(countList)):
            prevNum = self.getMaxCommonFactor(
                prevNum, countList[i])
            if prevNum < 2:
                return False
        return True

    def getMaxCommonFactor(self, num1, num2):
        while num1 > 0:
            num2 %= num1
            num1, num2 = num2, num1
        return num2
