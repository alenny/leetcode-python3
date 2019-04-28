class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        vals = [a, b, c]
        vals.sort()
        if vals[1] - vals[0] == 1 and vals[2] - vals[1] == 1:
            return [0, 0]
        minSteps = 1 if vals[1] - vals[0] <= 2 or vals[2] - vals[1] <= 2 else 2
        maxSteps = (vals[2] - vals[1] - 1) + (vals[1] - vals[0] - 1)
        return [minSteps, maxSteps]


sol = Solution()
ret = sol.numMovesStones(8, 1, 4)
print(ret)
ret = sol.numMovesStones(1, 2, 5)
print(ret)
ret = sol.numMovesStones(4, 3, 2)
print(ret)
