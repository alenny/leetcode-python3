class Solution:
    def minPatches(self, nums, n: int) -> int:
        target = 1
        patches = 0
        ni = 0
        NL = len(nums)
        # Note: when we add a patch - target,
        # all numbers from target+1 to target+target-1 can be formed by the array,
        # so we can set the new target to target+target.
        # when we find a bigger number at index i of nums, we set the new target to target + nums[i]
        while ni < NL and target <= n:
            if nums[ni] < target:
                target += nums[ni]
                ni += 1
            elif nums[ni] == target:
                target += target
                ni += 1
            else:
                # nums[ni] > target
                patches += 1
                target += target
        while target <= n:
            patches += 1
            target += target
        return patches


sol = Solution()
ret = sol.minPatches([1, 3], 6)   # 1
print(ret)
ret = sol.minPatches([1, 5, 10], 20)   # 2
print(ret)
ret = sol.minPatches([1, 2, 2], 5)   # 0
print(ret)
