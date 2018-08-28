class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.__searchHelper(nums, target, 0, len(nums) - 1)

    def __searchHelper(self, nums, target, begin, end):
        if begin > end:
            return -1
        mid = begin + end >> 1
        if nums[mid] == target:
            return mid
        return self.__searchHelper(nums, target, begin, mid - 1) if nums[mid] > target else self.__searchHelper(nums, target, mid + 1, end)
