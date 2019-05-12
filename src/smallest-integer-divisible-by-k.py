class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K & 1 == 0:
            return -1
        NL = 1
        N = 1
        remainSet = set()
        while True:
            remain = N % K
            if remain == 0:
                return NL
            if remain in remainSet:
                break
            remainSet.add(remain)
            NL += 1
            N = N * 10 + 1
        return -1


sol = Solution()
ret = sol.smallestRepunitDivByK(2)  # -1
ret = sol.smallestRepunitDivByK(3)  # 3
print(ret)