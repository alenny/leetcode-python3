class Solution:
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.lowNum, self.highNum = int(low), int(high)
        lenLow, lenHigh = len(low), len(high)
        self.leftMost = ['1', '6', '8', '9']
        self.rightMost = ['1', '9', '8', '6']
        middle = ['0', '1', '8']
        self.leftInter = ['0', '1', '6', '8', '9']
        self.rightInter = ['0', '1', '9', '8', '6']
        total = 0
        for ln in range(lenLow + 1, lenHigh):
            halfLn = ln >> 1
            count = len(self.leftMost)
            for i in range(1, halfLn):
                count *= len(self.leftInter)
            if ln & 1:
                count *= len(middle)
            total += count
        # lenLow
        if lenLow & 1:
            for m in middle:
                total += self.dfs(m, lenLow)
        else:
            total += self.dfs('', lenLow)
        # lenHigh
        if lenHigh != lenLow:
            if lenHigh & 1:
                for m in middle:
                    total += self.dfs(m, lenHigh)
            else:
                total += self.dfs('', lenHigh)
        return total

    def dfs(self, part, length):
        if len(part) == length:
            num = int(part)
            return 1 if num >= self.lowNum and num <= self.highNum else 0
        leftChoices, rightChoice = (self.leftMost, self.rightMost) \
            if length - len(part) == 2 \
            else (self.leftInter, self.rightInter)
        count = 0
        for i, l in enumerate(leftChoices):
            count += self.dfs(l + part + rightChoice[i], length)
        return count
