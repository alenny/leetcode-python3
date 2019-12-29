class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            digits = 1
            while n > 0:
                n = n // 10
                if n == 0:
                    break
                digits += 1
            if (digits & 1) == 0:
                ret += 1
        return ret
