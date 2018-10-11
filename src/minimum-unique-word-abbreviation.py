class Solution:
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        masks = []
        for s in dictionary:
            if len(s) != len(target):
                continue
            mask = 0
            for i in range(len(s)):
                if s[i] != target[i]:
                    mask |= 1 << i
            masks.append(mask)
        if len(masks) == 0:
            return str(len(target))
        binary = self.dfs(masks, 0, len(target), 0)[0]
        return self.makeAbbr(binary, target)

    def dfs(self, masks, binary, strLen, idx):
        if idx == strLen:
            for mask in masks:
                if mask & binary == mask:
                    return (0, strLen)
            return binary, self.countAbbrLen(binary, strLen)
        bit = 1 << idx
        binary += bit
        ret0 = self.dfs(masks, binary, strLen, idx + 1)
        binary -= bit
        ret1 = self.dfs(masks, binary, strLen, idx + 1)
        return ret1 if ret1[1] < ret0[1] else ret0

    def countAbbrLen(self, binary, strLen):
        abbrlen = 0
        countOne = 0
        for i in range(strLen):
            if binary & (1 << i):
                countOne += 1
                continue
            if countOne > 0:
                abbrlen += 1
                countOne = 0
            abbrlen += 1
        if countOne > 0:
            abbrlen += 1
        return abbrlen

    def makeAbbr(self, binary, target):
        parts = []
        countOne = 0
        for i in range(len(target)):
            if binary & (1 << i):
                countOne += 1
                continue
            if countOne > 0:
                parts.append(str(countOne))
                countOne = 0
            parts.append(target[i])
        if countOne > 0:
            parts.append(str(countOne))
        return ''.join(parts)


sol = Solution()
ret = sol.minAbbreviation("apple", ["blade"])
print(ret)
