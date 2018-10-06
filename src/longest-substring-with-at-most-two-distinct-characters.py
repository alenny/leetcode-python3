from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return len(s)
        distinct = 2
        countMap = defaultdict(int)
        left, right = 0, 1
        longest = 2
        countMap[s[0]] = 1
        while left < len(s) - longest and right < len(s):
            if len(countMap) < distinct or s[right] in countMap:
                countMap[s[right]] += 1
                right += 1
                longest = max(longest, right - left)
            else:
                # len(countMap) == distinct and not s[right] in countMap
                if countMap[s[left]] == 1:
                    countMap.pop(s[left])
                else:
                    countMap[s[left]] -= 1
                left += 1
        return longest
