class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [[0 for pos in range(9)] for level in range(5)]
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            val = nums[i] % 10
            pos = int(nums[i] / 10) % 10
            level = int(nums[i] / 100)
            count = counts[level][pos] if counts[level][pos] > 0 else 1
            total += val * count
            if level > 1:
                counts[level - 1][pos + 1 >> 1] += count
        return total


sol = Solution()
ret = sol.pathSum([113, 229, 349, 470, 485])
print(ret)
