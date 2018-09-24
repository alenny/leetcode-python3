from collections import defaultdict


class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        sums = []
        total = 0
        leftSumMap = defaultdict(list)
        for i in range(len(nums)):
            total += nums[i]
            sums.append(total)
            leftSumMap[total].append(i + 1)
        for k in range(len(nums) - 2, 4, -1):
            rightSum = sums[-1] - sums[k]
            if not rightSum in leftSumMap:
                continue
            iIndexes = leftSumMap[rightSum]
            for i in iIndexes:
                if i > k - 4:
                    break
                for j in range(i + 2, k - 1):
                    if sums[j - 1] - sums[i] == rightSum and sums[k - 1] - sums[j] == rightSum:
                        return True
        return False
