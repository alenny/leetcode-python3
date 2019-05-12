import math

class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        N = len(A)
        stack = [0]
        ret = -math.inf
        for j in range(1, N):
            while stack and A[j] >= A[stack[-1]]:
                i = stack.pop()
                ret = max(ret, A[i] + A[j] + i - j)
            if stack:
                i = stack[-1]
                ret = max(ret, A[i] + A[j] + i - j)
            stack.append(j)
        while len(stack) > 1:
            j = stack.pop()
            i = stack[-1]
            ret = max(ret, A[i] + A[j] + i - j)
        return ret
            
sol = Solution()
ret = sol.maxScoreSightseeingPair([8,1,5,2,6])
print(ret)