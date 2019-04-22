class Solution:
    def sortArray(self, nums):
        N = len(nums)

        def quick(l, r):
            if l >= r:
                return
            pivot, ri, wi = nums[r], l, l
            while ri < r:
                if nums[ri] < pivot:
                    nums[ri], nums[wi] = nums[wi], nums[ri]
                    wi += 1
                ri += 1
            nums[wi], nums[r] = nums[r], nums[wi]
            quick(l, wi - 1)
            quick(wi + 1, r)

        quick(0, N - 1)
        return nums


sol = Solution()
ret = sol.sortArray([5, 2, 3, 1, ])
print(ret)
