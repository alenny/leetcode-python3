from collections import defaultdict
import math


class CountNode:
    def __init__(self, count):
        self.count = count
        self.keyHead = KeyNode(math.nan, -1)
        self.keyTail = KeyNode(math.nan, -1)
        self.keyHead.next = self.keyTail
        self.keyTail.next = self.keyHead
        self.prev = None
        self.next = None


class KeyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.countHead = CountNode(0)
        self.countTail = CountNode(-1)
        self.countHead.next = self.countTail
        self.countTail.prev = self.countHead
        self.kvMap = dict()
        self.kcMap = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.kvMap:
            return -1
        self.incUsed(key)
        return self.kvMap[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if not key in self.kvMap:
            if len(self.kvMap) == self.capacity:
                self.evictLfu()
            self.kvMap[key] = KeyNode(key, value)
        else:
            self.kvMap[key].val = value
        self.incUsed(key)

    def incUsed(self, key):
        kNode = self.kvMap[key]
        if not key in self.kcMap:
            # put the first time
            if self.countHead.next.count != 1:
                self.insertNodeAfter(CountNode(1), self.countHead)
            self.insertNodeAfter(kNode, self.countHead.next.keyHead)
            self.kcMap[key] = self.countHead.next
        else:
            curCountNode = self.kcMap[key]
            self.removeNode(kNode)
            newCount = curCountNode.count + 1
            if curCountNode.next.count != newCount:
                self.insertNodeAfter(CountNode(newCount), curCountNode)
            self.insertNodeAfter(kNode, curCountNode.next.keyHead)
            self.kcMap[key] = curCountNode.next
            if curCountNode.keyHead.next == curCountNode.keyTail:
                self.removeNode(curCountNode)

    def evictLfu(self):
        leastCountNode = self.countHead.next
        kNode = leastCountNode.keyTail.prev
        self.removeNode(kNode)
        self.kvMap.pop(kNode.key)
        self.kcMap.pop(kNode.key)
        if leastCountNode.keyHead.next == leastCountNode.keyTail:
            self.removeNode(leastCountNode)

    def insertNodeAfter(self, newNode, oldNode):
        newNode.prev = oldNode
        newNode.next = oldNode.next
        newNode.prev.next = newNode.next.prev = newNode

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
