from collections import defaultdict


class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        begin, end = 0, 0
        map = defaultdict(int)
        longest = 0
        while end < len(tree):
            map[tree[end]] += 1
            end += 1
            if len(map) <= 2:
                continue
            longest = max(longest, end - begin - 1)
            while len(map) > 2:
                map[tree[begin]] -= 1
                if map[tree[begin]] == 0:
                    map.pop(tree[begin])
                begin += 1
        return max(longest, end - begin)


sol = Solution()
ret = sol.totalFruit([1, 2, 1])
print(ret)
