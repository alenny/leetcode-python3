class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2
        ret = sum(range(N - 3, -1, -4))
        ret += N * (N - 1) // (N - 2)
        for n in range(N - 4, 2, -4):
            ret -= n * (n - 1) // (n - 2)
        if N % 4 == 2:
            ret -= 2
        elif N % 4 == 1:
            ret -= 1
        return ret


sol = Solution()
ret = sol.clumsy(10)  # 12
ret = sol.clumsy(4)  # 7
print(ret)
