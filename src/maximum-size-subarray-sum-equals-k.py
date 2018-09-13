from collections import defaultdict


class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumsMap = defaultdict(list)
        sumsMap[0] = [0]
        sum = 0
        for i in range(1, len(nums) + 1):
            sum += nums[i - 1]
            sumsMap[sum].append(i)
        longest = 0
        for lowSum, lowCounts in sumsMap.items():
            highSum = lowSum + k
            if not highSum in sumsMap:
                continue
            highCounts = sumsMap[highSum]
            longest = max(longest, highCounts[-1] - lowCounts[0])
        return longest
