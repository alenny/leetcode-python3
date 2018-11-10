class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        # explanation: https://leetcode.com/problems/beautiful-array/discuss/186679/C%2B%2BJavaPython-Odd-%2B-Even-Pattern-O(N)
        ret = [1]
        while len(ret) < N:
            ret = [2 * x - 1 for x in ret if x <= (N + 1 >> 1)] \
                + [2 * x for x in ret if x <= (N >> 1)]
        return ret


sol = Solution()
ret = sol.beautifulArray(5)
print(ret)
