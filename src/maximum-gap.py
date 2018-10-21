import math


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N)
        N = len(nums)
        if N < 2:
            return 0
        minNum, maxNum = min(nums), max(nums)
        bucketSize = max(1, int((maxNum - minNum) / (N - 1)))
        bucketCount = int((maxNum - minNum) / bucketSize) + 1
        buckets = [[math.inf, -math.inf] for i in range(bucketCount)]
        for num in nums:
            bi = int((num - minNum) / bucketSize)
            buckets[bi][0] = min(buckets[bi][0], num)
            buckets[bi][1] = max(buckets[bi][1], num)
        maxGap = 0
        prevBi = 0
        while buckets[prevBi][0] == math.inf:
            prevBi += 1
        for i in range(prevBi + 1, len(buckets)):
            if buckets[i][0] == math.inf:
                continue
            maxGap = max(maxGap, buckets[i][0] - buckets[prevBi][1])
            prevBi = i
        return maxGap

    def maximumGapByRadixSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(k*N), k < logN, k is the loop turns
        if len(nums) < 2:
            return 0
        lvl = 1
        maxNum = max(nums)
        turns = int(math.log10(maxNum)) + 1
        buckets = [nums]
        for i in range(turns + 1):
            nextBuckets = [[] for i in range(10)]
            for bucket in buckets:
                for num in bucket:
                    bi = int(num / lvl) % 10
                    nextBuckets[bi].append(num)
            lvl *= 10
            buckets = nextBuckets
        maxGap = 0
        nums = buckets[0]
        for i in range(len(nums) - 1):
            maxGap = max(maxGap, nums[i + 1] - nums[i])
        return maxGap

    def maximumGapByComparisonSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N*logN)
        if len(nums) < 2:
            return 0
        nums.sort()
        maxGap = 0
        for i in range(len(nums) - 1):
            maxGap = max(maxGap, nums[i + 1] - nums[i])
        return maxGap


sol = Solution()
# ret = sol.maximumGap([1, 10000000])
ret = sol.maximumGap([1, 1, 1, 1])
print(ret)
