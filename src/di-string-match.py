class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ret = [0]
        low = high = 0
        for ch in S:
            if ch == 'I':
                high += 1
                ret.append(high)
            else:
                low -= 1
                ret.append(low)
        for i in range(len(ret)):
            ret[i] -= low
        return ret
