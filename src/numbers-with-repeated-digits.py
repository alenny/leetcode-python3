import math

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        if N < 10:
            return 0
        digits = list((map(int, str(N))))
        dc = len(digits)
        # f[i] means the count of rep-numbers with exact i digits,
        # INCLUDING leading zeros, e.g. 000-999 when i == 3
        f = [0, 0]
        # p[i] means the count of rep-numbers with exact i digits,
        # EXCLUDING leading zeros, e.g. 100-999 when i == 3
        p = [0, 0]
        for i in range(2, 10):
            tmp = (i - 1) * self.factorial(9, i - 2) + f[i - 1]
            p.append(9 * tmp)
            f.append(p[-1] + tmp)
        ret = 0
        for i in range(dc):
            ret += p[i]
        ds = set()
        jStart = 1
        for i in range(dc):
            for j in range(jStart, digits[i]):
                if j in ds:
                    ret += 10**(dc - i - 1)
                else:
                    # the two factorials here means the count of all combinations subtracts 
                    # the count of combinations which do not include any of the highest (i+1) digits
                    ret += f[dc - i - 1] + self.factorial(10, dc - i - 1) - self.factorial(10 - i - 1, dc - i - 1)
            jStart = 0
            if digits[i] in ds:
                tmp = 10**(dc - i - 1)
                ret += N - N // tmp * tmp + 1
                break
            ds.add(digits[i])
        return ret    


    def factorial(self, largest, count):
        ret = 1
        num = largest
        while count > 0:
            ret *= num
            num -= 1
            count -= 1
        return ret

sol = Solution()
# ret = sol.numDupDigitsAtMostN(10)
# ret = sol.numDupDigitsAtMostN(12)   # 1
# ret = sol.numDupDigitsAtMostN(20)   # 1
# ret = sol.numDupDigitsAtMostN(100)
# ret = sol.numDupDigitsAtMostN(1000)
# ret = sol.numDupDigitsAtMostN(10000)
ret = sol.numDupDigitsAtMostN(1962)  # 739
print(ret)