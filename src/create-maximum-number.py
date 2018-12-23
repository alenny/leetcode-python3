class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        L1, L2 = len(nums1), len(nums2)
        ret = None
        for l1 in range(max(0, k - L2), min(k, L1) + 1):
            l2 = k - l1
            temp = self.merge(self.findMaxSeq(nums1, l1),
                              self.findMaxSeq(nums2, l2))
            if not ret or temp > ret:
                ret = temp
        return ret

    def findMaxSeq(self, nums, length):
        seq, i, N = [], 0, len(nums)
        while len(seq) < length:
            maxIdx = N - (length - len(seq))
            top, topIdx = nums[i], i
            while i < maxIdx:
                i += 1
                if nums[i] > top:
                    top, topIdx = nums[i], i
            seq.append(top)
            i = topIdx + 1
        return seq

    def merge(self, arr1, arr2):
        i1, i2, l1, l2 = 0, 0, len(arr1), len(arr2)
        ret = []
        while i1 < l1 and i2 < l2:
            ii1, ii2 = i1, i2
            while ii1 < l1 and ii2 < l2 and arr1[ii1] == arr2[ii2]:
                ii1 += 1
                ii2 += 1
            if ii2 >= l2 or ii1 < l1 and ii2 < l2 and arr1[ii1] > arr2[ii2]:
                ret.append(arr1[i1])
                i1 += 1
            else:
                ret.append(arr2[i2])
                i2 += 1
        while i1 < l1:
            ret.append(arr1[i1])
            i1 += 1
        while i2 < l2:
            ret.append(arr2[i2])
            i2 += 1
        return ret

    def maxNumberDP(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        L1, L2 = len(nums1), len(nums2)
        dp = [[[[] for i2 in range(L2 + 1)]
               for i1 in range(L1 + 1)]
              for kk in range(k + 1)]
        for kk in range(1, k + 1):
            for i1 in range(kk, L1 + 1):
                dp[kk][i1][0] = max(
                    dp[kk][i1 - 1][0], [nums1[L1 - i1]] + dp[kk - 1][i1 - 1][0])
            for i2 in range(kk, L2 + 1):
                dp[kk][0][i2] = max(
                    dp[kk][0][i2 - 1], [nums2[L2 - i2]] + dp[kk - 1][0][i2 - 1])
            for total in range(kk, L1 + L2 + 1):
                for i1 in range(max(1, total - L2), min(L1 + 1, total)):
                    i2 = total - i1
                    dp[kk][i1][i2] = max(
                        dp[kk][i1][i2 - 1],
                        dp[kk][i1 - 1][i2],
                        [nums1[L1 - i1]] + dp[kk - 1][i1 - 1][i2],
                        [nums2[L2 - i2]] + dp[kk - 1][i1][i2 - 1])
        return dp[k][L1][L2]


sol = Solution()
# ret = sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
# ret = sol.maxNumber([6, 7], [6, 0, 4], 5)
ret = sol.maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2],15)
print(ret)
