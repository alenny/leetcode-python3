from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countMap = defaultdict(int)
        for ch in s:
            countMap[ch] += 1
        oddCount = 0
        for v in countMap.values():
            if v % 2 == 1:
                oddCount += 1
        return oddCount < 2
