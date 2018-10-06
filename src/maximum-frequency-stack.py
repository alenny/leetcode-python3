import math
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.stack = []
        self.countMap = defaultdict(int)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.countMap[x] += 1
        c = self.countMap[x]
        if c > len(self.stack):
            self.stack.append([])
        self.stack[c - 1].append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return math.nan
        ret = self.stack[-1].pop()
        if len(self.stack[-1]) == 0:
            self.stack.pop()
        if self.countMap[ret] == 1:
            self.countMap.pop(ret)
        else:
            self.countMap[ret] -= 1
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


class NumberNode:
    def __init__(self, val):
        self.val = val
        self.indexes = []
        self.prev = None
        self.next = None


class CountNode:
    def __init__(self, count):
        self.count = count
        self.head = NumberNode(math.nan)
        self.tail = NumberNode(math.nan)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.prev = None
        self.next = None


class FreqStackByLinkedList:

    def __init__(self):
        self.countHead = CountNode(0)
        self.countTail = CountNode(0)
        self.countHead.next = self.countTail
        self.countTail.prev = self.countHead
        self.countMap = dict()
        self.numMap = dict()
        self.nextIndex = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x in self.numMap:
            cur = self.numMap[x]
            curCountNode = self.countMap[len(cur.indexes)]
        else:
            cur, curCountNode = NumberNode(x), self.countTail
            self.numMap[x] = cur
        if curCountNode != self.countTail:
            self.removeNode(cur)
        cur.indexes.append(self.nextIndex)
        self.nextIndex += 1
        newCountNode = self.getOrCreateCountNode(
            len(cur.indexes), curCountNode)
        self.insertNodeAfter(cur, newCountNode.head)
        if curCountNode != self.countTail and curCountNode.head.next == curCountNode.tail:
            self.removeNode(curCountNode)
            self.countMap.pop(curCountNode.count)

    def pop(self):
        """
        :rtype: int
        """
        if self.countHead.next == self.countTail:
            return math.nan
        curCountNode = self.countHead.next
        cur = curCountNode.head.next
        self.removeNode(cur)
        if curCountNode.head.next == curCountNode.tail:
            self.removeNode(curCountNode)
            self.countMap.pop(curCountNode.count)
        cur.indexes.pop()
        if len(cur.indexes) == 0:
            self.numMap.pop(cur.val)
            return cur.val
        newCountNode = self.getOrCreateCountNode(
            len(cur.indexes), curCountNode.next)
        target = newCountNode.head.next
        while target != newCountNode.tail and target.indexes[-1] > cur.indexes[-1]:
            target = target.next
        self.insertNodeBefore(cur, target)
        return cur.val

    def getOrCreateCountNode(self, count, lessCountNode):
        if count in self.countMap:
            return self.countMap[count]
        newNode = CountNode(count)
        self.countMap[count] = newNode
        self.insertNodeBefore(newNode, lessCountNode)
        return newNode

    def removeNode(self, cur):
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def insertNodeBefore(self, newNode, oldNode):
        newNode.next = oldNode
        newNode.prev = oldNode.prev
        newNode.prev.next = newNode.next.prev = newNode

    def insertNodeAfter(self, newNode, oldNode):
        newNode.prev = oldNode
        newNode.next = oldNode.next
        newNode.prev.next = newNode.next.prev = newNode

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


stack = FreqStack()
stack.push(5)
stack.push(7)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(5)
ret = stack.pop()
ret = stack.pop()
ret = stack.pop()
ret = stack.pop()
print('ok')
