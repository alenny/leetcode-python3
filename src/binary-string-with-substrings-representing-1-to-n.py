class Solution:
    def queryString(self, S: str, N: int) -> bool:
        numSet = set()
        SL = len(S)
        for i in range(SL):
            if S[i] == '0':
                continue
            for nl in range(1, 31):
                x = int(S[i:i + nl], 2)
                if x > N:
                    break
                numSet.add(x)
        return len(numSet) == N

sol = Solution()
ret = sol.queryString("0110",  3)   # true
ret = sol.queryString("0110",  4)   # false
print(ret)
