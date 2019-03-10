class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]  # sums[i] is the sum of the first i numbers
        for n in nums:
            sums.append(sums[-1] + n)
        return self.__dnc(sums, lower, upper)[1]

    def __dnc(self, sums, lower, upper):
        N = len(sums)
        if N <= 1:
            return sums, 0
        half = N >> 1
        first, countFirst = self.__dnc(sums[:half], lower, upper)
        second, countSecond = self.__dnc(sums[half:], lower, upper)
        count = countFirst + countSecond
        NF, NS = len(first), len(second)
        merged = []
        li, mi, ui = 0, 0, 0
        for fi in range(NF):
            while li < NS and second[li] - first[fi] < lower:
                li += 1
            ui = max(ui, li)
            while ui < NS and second[ui] - first[fi] <= upper:
                ui += 1
            count += ui - li
            # merge sort
            while mi < NS and second[mi] < first[fi]:
                merged.append(second[mi])
                mi += 1
            merged.append(first[fi])
        while mi < NS:
            merged.append(second[mi])
            mi += 1
        return merged, count


sol = Solution()
ret = sol.countRangeSum([0, 0], 0, 0)
print(ret)
