class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            ret = []
            for x in nums:
                ret.append(b * x + c)
            if b < 0:
                ret.reverse()
            return ret
        # a != 0
        centerX = -b / (2 * a)
        ret = []
        right = 0
        while right < len(nums) and nums[right] < centerX:
            right += 1
        left = right - 1
        while left >= 0 and right < len(nums):
            if abs(nums[right] - centerX) < abs(nums[left] - centerX):
                ret.append(self.calResult(a, b, c, nums[right]))
                right += 1
            else:
                ret.append(self.calResult(a, b, c, nums[left]))
                left -= 1
        while left >= 0:
            ret.append(self.calResult(a, b, c, nums[left]))
            left -= 1
        while right < len(nums):
            ret.append(self.calResult(a, b, c, nums[right]))
            right += 1
        if a < 0:
            ret.reverse()
        return ret

    def calResult(self, a, b, c, x):
        return a * x * x + b * x + c

sol = Solution()
ret = sol.sortTransformedArray([-99,-94,-90,-88,-84,-83,-79,-68,-58,-52,-52,-50,-47,-45,-35,-29,-5,-1,9,12,13,25,27,33,36,38,40,46,47,49,57,57,61,63,73,75,79,97,98],-2,44,-56)
print(ret)