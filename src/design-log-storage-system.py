class StorageNode:
    def __init__(self):
        self.indexes = []
        self.children = dict()


class LogSystem:

    def __init__(self):
        self.logs = StorageNode()
        self.granularity = {'Year': 0, 'Month': 1,
                            'Day': 2, 'Hour': 3, 'Minute': 4, 'Second': 5}
        self.minPartVal = [2000, 1, 1, 0, 0, 0]
        self.maxPartVal = [2017, 12, 31, 23, 59, 59]

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        timeParts = self.extractTime(timestamp)
        cur = self.logs
        cur.indexes.append(id)
        for i in range(6):
            part = timeParts[i]
            if not part in cur.children:
                cur.children[part] = StorageNode()
            cur = cur.children[part]
            cur.indexes.append(id)

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        startParts = self.extractTime(s)
        endParts = self.extractTime(e)
        graIdx = self.granularity[gra]
        fdpi = 0    # firstDiffPartIdx
        while fdpi <= graIdx and startParts[fdpi] == endParts[fdpi]:
            fdpi += 1
        if fdpi > graIdx:
            # all effective parts are the same
            cur = self.logs
            for i in range(graIdx + 1):
                if not startParts[i] in cur.children:
                    return []
                cur = cur.children[startParts[i]]
            return cur.indexes
        ret = []
        cur = self.logs
        for i in range(fdpi):
            if not startParts[i] in cur.children:
                return []
            cur = cur.children[startParts[i]]
        for partVal in range(startParts[fdpi] + 1, endParts[fdpi]):
            if partVal in cur.children:
                ret.extend(cur.children[partVal].indexes)
        startCur = cur.children[startParts[fdpi]] \
            if startParts[fdpi] in cur.children else None
        endCur = cur.children[endParts[fdpi]] \
            if endParts[fdpi] in cur.children else None
        for i in range(fdpi + 1, graIdx + 1):
            if startCur:
                for partVal in range(startParts[i] + 1, self.maxPartVal[i] + 1):
                    if partVal in startCur.children:
                        ret.extend(startCur.children[partVal].indexes)
                startCur = startCur.children[startParts[i]] \
                    if startParts[i] in startCur.children else None
            if endCur:
                for partVal in range(self.minPartVal[i], endParts[i]):
                    if partVal in endCur.children:
                        ret.extend(endCur.children[partVal].indexes)
                endCur = endCur.children[endParts[i]] \
                    if endParts[i] in endCur.children else None
        if startCur:
            ret.extend(startCur.indexes)
        if endCur:
            ret.extend(endCur.indexes)
        return ret

    def extractTime(self, timestamp):
        parts = timestamp.split(':')
        return [int(p) for p in parts]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

sys = LogSystem()
sys.put(1, "2017:01:01:23:59:59")
sys.put(2, "2017:01:01:22:59:59")
sys.put(3, "2016:01:01:00:00:00")
ret = sys.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")
ret = sys.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
print('ok')
