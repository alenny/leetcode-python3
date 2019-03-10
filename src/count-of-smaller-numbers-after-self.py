class Solution:
    def countSmaller(self, nums):
        N = len(nums)
        items = [(n, i) for i, n in enumerate(nums)]
        ret = [0] * N
        self.dncMergeSort(items, ret)
        return ret

    def dncMergeSort(self, items, ret):
        N = len(items)
        if N <= 1:
            return items
        half = N >> 1
        left = self.dncMergeSort(items[:half], ret)
        right = self.dncMergeSort(items[half:], ret)
        merged = []
        NL, NR, li, ri = len(left), len(right), 0, 0
        while li < NL and ri < NR:
            if left[li][0] <= right[ri][0]:
                merged.append(left[li])
                ret[left[li][1]] += len(merged) - 1 - li
                li += 1
            else:
                merged.append(right[ri])
                ri += 1
        while li < NL:
            merged.append(left[li])
            ret[left[li][1]] += len(merged) - 1 - li
            li += 1
        while ri < NR:
            merged.append(right[ri])
            ri += 1
        return merged


sol = Solution()
ret = sol.countSmaller([5, 2, 6, 1])
print(ret)
