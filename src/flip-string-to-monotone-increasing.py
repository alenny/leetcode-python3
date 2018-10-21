class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        prevZeros = [0]
        prevOnes = [0]
        totalZeros, totalOnes = 0, 0
        for ch in S:
            if ch == '0':
                totalZeros += 1
            if ch == '1':
                totalOnes += 1
            prevZeros.append(totalZeros)
            prevOnes.append(totalOnes)
        minFlips = N
        for i in range(N + 1):
            minFlips = min(
                minFlips, prevOnes[i] + (prevZeros[N] - prevZeros[i]))
        return minFlips


sol = Solution()
ret = sol.minFlipsMonoIncr('00011000')
print(ret)
