from collections import OrderedDict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.window = 300   # 5 minutes
        self.groupLen = 100
        self.groups = OrderedDict()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        groupKey = self.getGroupKey(timestamp)
        if not groupKey in self.groups:
            # records and hits of group
            self.groups[groupKey] = [OrderedDict(), 0]
        idx = self.getIndexInGroup(timestamp)
        if not idx in self.groups[groupKey][0]:
            self.groups[groupKey][0][idx] = 0
        self.groups[groupKey][0][idx] += 1
        self.groups[groupKey][1] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        totalHits = 0
        firstTimeStamp = timestamp - self.window + 1
        for groupTime, group in reversed(self.groups.items()):
            if groupTime + self.window - 1 < firstTimeStamp:
                break
            if groupTime >= firstTimeStamp:
                totalHits += group[1]
                continue
            for time, hits in reversed(group[0].items()):
                if time + groupTime < firstTimeStamp:
                    break
                totalHits += hits
        return totalHits

    def getGroupKey(self, timestamp):
        return int(timestamp / self.groupLen) * self.groupLen

    def getIndexInGroup(self, timestamp):
        return timestamp % self.groupLen

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
ret = obj.getHits(4)
obj.hit(300)
ret = obj.getHits(300)
ret = obj.getHits(301)
print(ret)
