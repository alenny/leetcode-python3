class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] < target:
                    total += k - j
                    j += 1
                else:
                    k -= 1
        return total

    def threeSumSmallerN2LogN(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                limit = target - nums[i] - nums[j]
                if limit < nums[j]:
                    break
                pos = self.binarySearch(nums, limit, 0, len(nums) - 1)
                if pos < 0:
                    break
                total += max(0, pos - j)
        return total

    def binarySearch(self, nums, n, begin, end):
        # find the last number less than n
        if begin > end:
            return -1
        if begin == end:
            return begin if nums[begin] < n else -1
        mid = begin + end >> 1
        if nums[mid] < n and (mid == len(nums) - 1 or nums[mid + 1] >= n):
            return mid
        return self.binarySearch(nums, n, mid + 1, end) if nums[mid] < n else self.binarySearch(nums, n, begin, mid - 1)


sol = Solution()
#ret = sol.threeSumSmaller([0, -4, -1, 1, -1, 2], -5)
#ret = sol.threeSumSmaller([-2, 0, 1, 3], 2)
ret = sol.threeSumSmaller([1, 1, -2], 1)
