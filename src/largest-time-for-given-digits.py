class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        idxSet = set([0, 1, 2, 3])
        arr = self.helper(A, idxSet, [])
        return '' if arr == [-1, -1] else '{0:02d}:{1:02d}'.format(*arr)

    def helper(self, A, idxSet, parts):
        if len(parts) == 4:
            hour, minute = parts[0] * 10 + parts[1], parts[2] * 10 + parts[3]
            return [hour, minute] if hour < 24 and minute < 60 else [-1, -1]
        maxTime = [-1, -1]
        for i in idxSet:
            parts.append(A[i])
            t = self.helper(A, idxSet - set([i]), parts)
            maxTime = max(maxTime, t)
            parts.pop()
        return maxTime
