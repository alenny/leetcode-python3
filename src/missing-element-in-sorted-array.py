from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        N = len(nums)
        minNum = nums[0]
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            missing = nums[mid] - minNum - mid
            if missing >= k:
                r = mid - 1
            else:
                l = mid + 1
        firstLessThanK = max(0, min(l, r))
        
        # Simplified from: return nums[firstLessThanK] + (k - (nums[firstLessThanK] - nums[0] - firstLessThanK))
        return k + nums[0] + firstLessThanK

sol = Solution()
ret = sol.missingElement([4,7,9,10], 1)
print(ret)
ret = sol.missingElement([746421,1033196,1647541,4775111,7769817,8030384], 10)
print(ret)
