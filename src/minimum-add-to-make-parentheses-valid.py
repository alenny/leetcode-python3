class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        leftCount, rightCount = 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                leftCount += 1
            else:
                rightCount += 1
                if rightCount > leftCount:
                    leftCount += 1
        total = leftCount + rightCount - len(S)
        leftCount, rightCount = 0, 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '(':
                leftCount += 1
                if leftCount > rightCount:
                    rightCount += 1
            else:
                rightCount += 1
        total += leftCount + rightCount - len(S)
        return total
