from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        if N < 3:
            return 0
        dp2 = [defaultdict(int) for _ in range(N)]
        dp3 = [defaultdict(int) for _ in range(N)]
        dp2[1][A[1] - A[0]] += 1
        for i in range(2, N):
            dp2[i][A[i] - A[0]] += 1
            for j in range(1, i):
                diff = A[i] - A[j]
                if diff in dp2[j]:
                    dp3[i][diff] += dp2[j][diff]
                    dp2[i][diff] += dp2[j][diff] + 1
                else:
                    dp2[i][diff] += 1
        total = 0
        for c3map in dp3:
            for count in c3map.values():
                total += count
        return total


sol = Solution()
# ret = sol.numberOfArithmeticSlices([2, 4, 6, 8, 10])
# print(ret)
# ret = sol.numberOfArithmeticSlices([1, 1, 1, 1, 1])
# print(ret)
ret = sol.numberOfArithmeticSlices([2, 2, 3, 4])
print(ret)
