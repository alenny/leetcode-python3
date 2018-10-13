class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        opStack = []
        numStack = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == ')' or s[i] == '*' or s[i] == '/':
                opStack.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                # todo: finish all * and / in stack
                while len(opStack) > 0 and (opStack[-1] == '*' or opStack[-1] == '/'):
                    self.computeOnStack(opStack, numStack)
                opStack.append(s[i])
            elif s[i] == '(':
                # todo: finish all ops in stack until meeting ) and pop )
                while opStack[-1] != ')':
                    self.computeOnStack(opStack, numStack)
                opStack.pop()   # pop ')'
            elif s[i] != ' ':
                # numbers
                numEnd = i
                while i >= 0 and s[i] >= '0' and s[i] <= '9':
                    i -= 1
                numStack.append(int(s[i + 1:numEnd + 1]))
                i += 1
            i -= 1
        while len(opStack) > 0:
            self.computeOnStack(opStack, numStack)
        return numStack[0]

    def computeOnStack(self, opStack, numStack):
        numStack.append(self.compute(
            opStack.pop(), numStack.pop(), numStack.pop()))

    def compute(self, op, firstNum, secondNum):
        if op == '+':
            return firstNum + secondNum
        if op == '-':
            return firstNum - secondNum
        if op == '*':
            return firstNum * secondNum
        # '/'
        return int(firstNum / secondNum)


sol = Solution()
ret = sol.calculate('1 + 1')
