from collections import defaultdict
from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        countMap = defaultdict(int)
        for a in A:
            countMap[a] += 1
        minA = min(A)
        K -= 1
        while K > minA:
            for a in A:
                b = K - a
                if b != a and b in countMap or b == a and countMap[b] > 1:
                    return K
            K -= 1
        return -1


sol = Solution()
ret = sol.twoSumLessThanK([254, 914, 110, 900, 147, 441, 209, 122, 571, 942, 136, 350, 160, 127, 178, 839, 201, 386, 462, 45, 735, 467, 153,
                           415, 875, 282, 204, 534, 639, 994, 284, 320, 865, 468, 1, 838, 275, 370, 295, 574, 309, 268, 415, 385, 786, 62, 359, 78, 854, 944], 200)
print(ret)
