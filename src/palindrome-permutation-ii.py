from collections import defaultdict


class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
        oddCh = ''
        chs = list(mp.keys())
        for ch in chs:
            if mp[ch] & 1:
                if oddCh:
                    return []
                oddCh = ch
            mp[ch] >>= 1
        if oddCh and not (len(s) & 1):
            return []
        ret = []
        self.findResults(mp, chs,  '', len(s) >> 1, oddCh, ret)
        return ret

    def findResults(self, mp, chs, currHalf, halfLen, oddCh, ret):
        if len(currHalf) == halfLen:
            ret.append(currHalf + oddCh + currHalf[::-1])
            return
        for ch in chs:
            if mp[ch] == 0:
                continue
            mp[ch] -= 1
            self.findResults(mp, chs, currHalf + ch, halfLen, oddCh, ret)
            mp[ch] += 1


sol = Solution()
ret = sol.generatePalindromes('aabb')
