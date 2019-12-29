class Solution:
    def toHexspeak(self, num: str) -> str:
        n = int(num)
        codeA = ord('A')
        ret = []
        while n > 0:
            d = n % 16
            if d > 1 and d < 10:
                return 'ERROR'
            ret.append('O' if d == 0 else ('I' if d == 1 else chr(codeA + d - 10)))
            n = n // 16
        return ''.join(reversed(ret))

sol = Solution()
ret = sol.toHexspeak(747823223228)        