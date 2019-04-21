class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        AL = len(A)

        def getSubarraySums(A, N):
            sums = [0]
            for i in range(N):
                sums[0] += A[i]
            for i in range(N, AL):
                idx = i - N + 1
                sums.append(sums[idx - 1] - A[idx - 1] + A[i])
            return sums

        subL = getSubarraySums(A, L)
        subM = getSubarraySums(A, M)
        maxSum = 0
        for i in range(len(subL)):
            for j in range(len(subM)):
                if i <= j < i + L or j <= i < j + M:
                    continue
                maxSum = max(maxSum, subL[i] + subM[j])
        return maxSum


sol = Solution()
ret = sol.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)
print(ret)
