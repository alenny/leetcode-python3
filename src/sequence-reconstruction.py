class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        maxNum = len(org)
        relSet = set()
        posMap = [-1 for i in range(maxNum + 1)]
        posMap[org[0]] = 0
        for i in range(1, maxNum):
            posMap[org[i]] = i
            relSet.add(str(org[i - 1]) + ',' + str(org[i]))
        noSeq = True
        for seq in seqs:
            if len(seq) == 0:
                continue
            noSeq = False
            if len(seq) == 1:
                if not self.checkNum(maxNum, seq[0]):
                    return False
                continue
            if not self.checkNum(maxNum, seq[0]):
                return False
            for i in range(1, len(seq)):
                if not self.checkNum(maxNum, seq[i]) or posMap[seq[i - 1]] >= posMap[seq[i]]:
                    return False
                setKey = str(seq[i - 1]) + ',' + str(seq[i])
                if setKey in relSet:
                    relSet.remove(setKey)
        return True if len(relSet) == 0 and not noSeq else False

    def checkNum(self, maxNum, num):
        return num <= maxNum and num >= 1


sol = Solution()
ret = sol.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]])
print(ret)
