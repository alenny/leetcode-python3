from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A):
        # DP
        N = len(A)
        dp = [{}, {A[1] - A[0]: 2}]
        longest = 2
        for i in range(2, N):
            dp.append(defaultdict(int))
            dp[i][A[i] - A[0]] = 2
            for j in range(1, i):
                interval = A[i] - A[j]
                if not interval in dp[j]:
                    dp[i][interval] = max(dp[i][interval], 2)
                    continue
                dp[i][interval] = max(dp[i][interval], dp[j][interval] + 1)
                longest = max(longest, dp[i][interval])
        return longest

    def longestArithSeqLengthForce(self, A) -> int:
        N = len(A)
        posMap = defaultdict(list)
        for i, x in enumerate(A):
            posMap[x].append(i)
        maxL = 2
        for i, x in enumerate(A):
            for j in range(i + 1, N):
                diff = A[j] - x
                pi = j
                L = 2
                while True:
                    nv = A[pi] + diff
                    if not nv in posMap:
                        break
                    ni = -1
                    for nii in posMap[nv]:
                        if nii > pi:
                            ni = nii
                            break
                    if ni == -1:
                        break
                    L += 1
                    pi = ni
                maxL = max(maxL, L)
        return maxL


sol = Solution()
# ret = sol.longestArithSeqLength([3, 6, 9, 12])
ret = sol.longestArithSeqLength([9, 4, 7, 2, 10])
print(ret)
