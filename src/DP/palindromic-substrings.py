class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        total = N
        dp0 = [True] * N
        dp1 = [True] * N
        for ln in range(2, N + 1):
            for left in range(0, N - ln + 1):
                dp0[left] = dp0[left + 1] and s[left] == s[left + ln - 1]
                if dp0[left]:
                    total += 1
            dp0, dp1 = dp1, dp0
        return total


sol = Solution()
ret = sol.countSubstrings("xkjkqlajprjwefilxgpdpebieswu")
print(ret)
