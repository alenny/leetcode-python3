import math


class Solution:
    def baseNeg2(self, N: int) -> str:
        ones = []
        self._helper(N, ones)
        if not ones:
            return '0'
        ret = ['0'] * (ones[0] + 1)
        for pos in ones:
            ret[pos] = '1'
        return ''.join(reversed(ret))

    def _helper(self, N, ones):
        if N == 0:
            return True
        if N == 1:
            if ones and ones[-1] == 0:
                return False
            ones.append(0)
            return True
        isNeg = True if N < 0 else False
        up = math.ceil(math.log2(abs(N)))
        isUpEven = up % 2 == 0
        if isNeg and isUpEven or not isNeg and not isUpEven:
            up += 1
        low = up - 2
        if not ones or up < ones[-1]:
            ones.append(up)
            if self._helper(N - (-2)**up, ones):
                return True
            ones.pop()
        if not ones or low < ones[-1]:
            ones.append(low)
            if self._helper(N - (-2)**low, ones):
                return True
            ones.pop()
        return False


sol = Solution()
ret = sol.baseNeg2(54)
print(ret)
ret = sol.baseNeg2(2)
print(ret)
ret = sol.baseNeg2(3)
print(ret)
ret = sol.baseNeg2(4)
print(ret)
ret = sol.baseNeg2(5)
print(ret)
ret = sol.baseNeg2(-1)
print(ret)
ret = sol.baseNeg2(-5)
print(ret)
