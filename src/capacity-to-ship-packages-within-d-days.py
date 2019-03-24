class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + right >> 1
            curSum = 0
            daysNeeded = 1
            for w in weights:
                if curSum + w > mid:
                    daysNeeded += 1
                    curSum = w
                else:
                    curSum += w
            if daysNeeded > D:
                left = mid + 1
            else:
                right = mid
        return left

sol = Solution()
ret = sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)     # 15
ret = sol.shipWithinDays([3,2,2,4,1,4], 3)     # 6
print(ret)