class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        beginIpNum = self.ipToInt(ip)
        endIpNum = beginIpNum + n - 1
        pos = 31
        while pos > 0:
            mask = 1 << pos
            if (beginIpNum & mask) ^ (endIpNum & mask) != 0:
                break
            pos -= 1
        pos += 1
        return self.handle(beginIpNum, endIpNum, pos)

    def handle(self, beginIpNum, endIpNum, pos):
        thisRange = ''
        thisPos = pos
        begin = beginIpNum
        end = endIpNum
        while True:
            begin = (0xffffffff << thisPos) & beginIpNum
            end = begin + (1 << thisPos) - 1
            if begin >= beginIpNum and end <= endIpNum:
                thisRange = self.intToIp(begin) + '/' + str(32 - thisPos)
                break
            thisPos -= 1
        ranges = []
        if begin > beginIpNum:
            ranges += self.handle(beginIpNum, begin - 1, pos)
        ranges.append(thisRange)
        if end < endIpNum:
            ranges += self.handle(end + 1, endIpNum, pos)
        return ranges

    def ipToInt(self, ip):
        parts = ip.split('.')
        num = 0
        move = 24
        for p in parts:
            num += int(p) << move
            move -= 8
        return num

    def intToIp(self, val):
        mask = 0xff
        parts = []
        for i in range(3, -1, -1):
            parts.append(str((val >> i * 8) & mask))
        return '.'.join(parts)


sol = Solution()
#ret = sol.ipToCIDR("255.0.0.7", 10)
ret = sol.ipToCIDR("60.166.253.147", 12)
