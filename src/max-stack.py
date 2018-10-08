import heapq
from collections import defaultdict
import math


class StackNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.numToNodes = defaultdict(list)
        self.head = StackNode(math.nan)
        self.tail = StackNode(math.nan)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        newNode = StackNode(x)
        self.insertNodeAfter(newNode, self.head)
        if not x in self.numToNodes:
            heapq.heappush(self.maxHeap, -x)
        self.numToNodes[x].append(newNode)

    def pop(self):
        """
        :rtype: int
        """
        node = self.head.next
        self.removeNode(node)
        self.numToNodes[node.val].pop()
        if len(self.numToNodes[node.val]) == 0:
            self.numToNodes.pop(node.val)
        return node.val

    def top(self):
        """
        :rtype: int
        """
        return self.head.next.val

    def peekMax(self):
        """
        :rtype: int
        """
        val = -self.maxHeap[0]
        while not val in self.numToNodes:
            heapq.heappop(self.maxHeap)
            val = -self.maxHeap[0]
        return val

    def popMax(self):
        """
        :rtype: int
        """
        val = -self.maxHeap[0]
        while not val in self.numToNodes:
            heapq.heappop(self.maxHeap)
            val = -self.maxHeap[0]
        node = self.numToNodes[val].pop()
        self.removeNode(node)
        if len(self.numToNodes[val]) == 0:
            self.numToNodes.pop(val)
        return val

    def insertNodeAfter(self, newNode, oldNode):
        newNode.next = oldNode.next
        newNode.prev = oldNode
        newNode.prev.next = newNode.next.prev = newNode

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(6)
ret = obj.peekMax()
ret = obj.popMax()
ret = obj.popMax()
ret = obj.top()
print('ok')
