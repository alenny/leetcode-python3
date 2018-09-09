
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums), 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i >= len(nums) - 1:
                break
            if nums[i + 1] > nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


sol = Solution()
ret = [3, 5, 2, 1, 6, 4]
sol.wiggleSort(ret)
