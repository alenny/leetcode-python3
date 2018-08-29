class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        aCode = ord('a')
        groupSet = set()
        for s in A:
            counts = [[0 for i in range(26)] for j in range(2)]
            for i in range(len(s)):
                counts[i % 2][ord(s[i]) - aCode] += 1
            groupSet.add(str(counts))
        return len(groupSet)
