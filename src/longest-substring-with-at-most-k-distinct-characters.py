from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        countMap = defaultdict(int)
        l, r = 0, 0
        longest = 0
        while l < len(s) and r < len(s):
            if len(countMap) < k or s[r] in countMap:
                countMap[s[r]] += 1
                r += 1
                longest = max(longest, r - l)
                continue
            while len(countMap) == k:
                countMap[s[l]] -= 1
                if countMap[s[l]] == 0:
                    countMap.pop(s[l])
                l += 1
        return longest
