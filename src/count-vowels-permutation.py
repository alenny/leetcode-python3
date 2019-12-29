class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # im = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        dp = [[0] * 5 for i in range(n + 1)]
        dp[1][0] = dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = 1
        for i in range(2, n + 1):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][3] = dp[i - 1][2]
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
        return sum(dp[n]) % (10**9 + 7)