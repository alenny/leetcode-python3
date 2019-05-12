class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        sums = [0]
        for a in A:
            sums.append(sums[-1] + a)
        oneThird = sums[-1] / 3
        if oneThird != int(oneThird):
            return False
        j = 0
        found = 0
        for i in range(len(sums)):
            if sums[i] - sums[j] == oneThird:
                found += 1
                if found == 2:
                    return True
                j = i
        return False

sol = Solution()
ret = sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) 
print(ret)