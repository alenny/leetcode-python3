class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        SL = len(A[0])
        dp = [0] * SL
        for col in range(1, SL):
            dp[col] = col
            for c in range(col):
                fit = True
                for a in A:
                    if a[col] < a[c]:
                        fit = False
                        break
                if fit:
                    dp[col] = min(dp[col], dp[c] + col - c - 1)
        minDeletion = SL - 1
        for i, x in enumerate(dp):
            minDeletion = min(minDeletion, x + SL - i - 1)
        return minDeletion


sol = Solution()
ret = sol.minDeletionSize(["aaababa", "ababbaa"])
print(ret)
