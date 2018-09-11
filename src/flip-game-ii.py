class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        status = []
        consecutivePlus = 0
        for ch in s:
            if ch == '+':
                consecutivePlus += 1
            else:
                if consecutivePlus > 1:
                    status.append(consecutivePlus)
                consecutivePlus = 0
        if consecutivePlus > 1:
            status.append(consecutivePlus)
        cache = dict()
        return self.win(status, cache)

    def win(self, status, cache):
        key = self.statusToKey(status)
        if key in cache:
            return cache[key]
        canWin = False
        for i in range(len(status)):
            consecutive = status[i]
            newStatus = status[0:i] + status[i + 1:]
            for left in range(consecutive - 1):
                appendCount = 0
                if left >= 2:
                    newStatus.append(left)
                    appendCount += 1
                right = consecutive - left - 2
                if right >= 2:
                    newStatus.append(right)
                    appendCount += 1
                if not self.win(newStatus, cache):
                    canWin = True
                    break
                for j in range(appendCount):
                    newStatus.pop()
            if canWin:
                break
        cache[key] = canWin
        return canWin

    def statusToKey(self, status):
        return str(sorted(status))


sol = Solution()
ret = sol.canWin("++++--++++")
