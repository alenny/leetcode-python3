class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lastOneCount = 0
        longest = 1
        while i < len(nums):
            zeroBegin = i
            while i < len(nums) and nums[i] == 0:
                i += 1
            zeroCount = i - zeroBegin
            oneBegin = i
            while i < len(nums) and nums[i] == 1:
                i += 1
            oneCount = i - oneBegin
            if zeroCount != 1:
                longest = max(longest, oneCount + (1 if i < len(nums) else 0))
            else:
                longest = max(longest, lastOneCount + 1 + oneCount)
            lastOneCount = oneCount
        return longest
