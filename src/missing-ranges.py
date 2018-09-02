import math


class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges = [[lower, upper]]
        lastNum = math.nan
        for n in nums:
            if n == lastNum:
                continue
            lastNum = n
            currRange = ranges[-1]
            if n == currRange[0]:
                if currRange[0] == currRange[1]:
                    ranges.pop()
                else:
                    currRange[0] += 1
            elif n == currRange[1]:
                currRange[1] -= 1
            else:
                ranges.append([n + 1, currRange[1]])
                currRange[1] = n - 1
        output = []
        for rg in ranges:
            if rg[0] == rg[1]:
                output.append(str(rg[0]))
            else:
                output.append(str(rg[0]) + '->' + str(rg[1]))
        return output


sol = Solution()
sol.findMissingRanges([1, 1, 1, ], 1, 1)
