class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ss = list(S)
        if K == 1:
            minS = S
            for i in range(len(S) - 1):
                sx = ''.join(ss[i + 1:] + ss[:i + 1])
                if sx < minS:
                    minS = sx
            return minS
        ss.sort()
        return ''.join(ss)
