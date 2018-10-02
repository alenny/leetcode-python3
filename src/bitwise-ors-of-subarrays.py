class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = set([A[0]])
        prev = set([A[0]])
        for i in range(1, len(A)):
            # cur will only have 30 values at most
            ret.add(A[i])
            cur = set([A[i]])
            for x in prev:
                y = x | A[i]
                cur.add(y)
                ret.add(y)
            prev = cur
        return len(ret)


sol = Solution()
ret = sol.subarrayBitwiseORs([1, 1, 2])
print(ret)
