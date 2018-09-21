class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        return self.parseHelper(expression, 0)[0]

    def parseHelper(self, expression, begin):
        if begin == len(expression) - 1 or expression[begin + 1] != '?':
            return expression[begin], begin + 1
        leftVal, leftNext = self.parseHelper(expression, begin + 2)
        rightVal, rightNext = self.parseHelper(expression, leftNext + 1)
        return (leftVal, rightNext) if expression[begin] == 'T' else (rightVal, rightNext)


sol = Solution()
ret = sol.parseTernary("F?1:T?4:5")
print(ret)
