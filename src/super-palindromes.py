import math


class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        minimum = math.ceil(math.sqrt(int(L)))
        maximum = math.floor(math.sqrt(int(R)))
        minText = str(minimum)
        leftText = minText[:math.ceil(len(minText) / 2)]
        leftNum = int(leftText)
        rightLen = len(minText) - len(leftText)
        supers = []
        while True:
            num = int(leftText + leftText[:rightLen][::-1])
            nextLeftNum = leftNum + 1
            nextLeftText = str(nextLeftNum)
            leftNum, leftText, rightLen = (nextLeftNum, nextLeftText, rightLen) \
                if len(nextLeftText) == len(leftText) or rightLen == len(leftText) \
                else (int(nextLeftNum / 10), nextLeftText[:-1], rightLen + 1)
            if num > maximum:
                break
            if num >= minimum and self.isPalindrome(num * num):
                supers.append(num)
        return len(supers)

    def isPalindrome(self, num):
        sqText = str(num)
        return sqText == sqText[::-1]


sol = Solution()
ret = sol.superpalindromesInRange('1', '1000000000000000000')
print(ret)
