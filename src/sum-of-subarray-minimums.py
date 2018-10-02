import math
from collections import defaultdict


class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        modulo = 10**9 + 7
        stack = []
        totalSum = 0
        for r, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                i = stack.pop()
                l = stack[-1] if stack else -1
                totalSum = (totalSum + A[i] * (r - i) * (i - l)) % modulo
            stack.append(r)
        while stack:
            i = stack.pop()
            l = stack[-1] if stack else -1
            totalSum = (totalSum + A[i] * (len(A) - i) * (i - l)) % modulo
        return totalSum

    def sumSubarrayMinsByCountingLeftAndRight(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        modulo = 10**9 + 7
        leftLens = [0] * n
        rightLens = [0] * n
        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > A[i]:
                count += stack.pop()[1]
            leftLens[i] = count
            stack.append((A[i], count))
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= A[i]:
                count += stack.pop()[1]
            rightLens[i] = count
            stack.append((A[i], count))
        return sum(a * l * r for a, l, r in zip(A, leftLens, rightLens)) % modulo

    def sumSubarrayMinsByDivideConquer(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.modulo = pow(10, 9) + 7
        return self.sumHelper(A, 0, len(A) - 1)

    def sumHelper(self, A, begin, end):
        if begin > end:
            return 0
        minimum = math.inf
        minIdx = -1
        for i in range(begin, end + 1):
            if A[i] < minimum:
                minimum = A[i]
                minIdx = i
        sumMin = (minIdx - begin + 1) * \
            (end - minIdx + 1) * minimum % self.modulo
        return (self.sumHelper(A, begin, minIdx - 1) + sumMin + self.sumHelper(A, minIdx + 1, end)) % self.modulo


sol = Solution()
ret = sol.sumSubarrayMins([3, 1, 2, 4])
print(ret)
