class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + right >> 1
            totalHours = 0
            for count in piles:
                totalHours += (count - 1) // mid + 1
            if totalHours > H:
                left = mid + 1
            else:
                right = mid
        return left

sol = Solution()
ret = sol.minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818)
print(ret)