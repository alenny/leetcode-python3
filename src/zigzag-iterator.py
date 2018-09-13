class Node:
    def __init__(self, vec):
        self.vec = vec
        self.idx = 0
        self.prev = None
        self.next = None


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.addVector(v1)
        self.addVector(v2)
        self.cursor = self.head
        self.goToNext()

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        ret = self.cursor.vec[self.cursor.idx]
        self.goToNext()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor != self.tail

    def addVector(self, vec):
        if len(vec) == 0:
            return
        newNode = Node(vec)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        newNode.prev.next = newNode.next.prev = newNode

    def goToNext(self):
        if self.cursor != self.head:
            self.cursor.idx += 1
            if self.cursor.idx >= len(self.cursor.vec):
                self.cursor.prev.next = self.cursor.next
                self.cursor.next.prev = self.cursor.prev
                if self.head.next == self.tail:
                    self.cursor = self.tail
                    return
        self.cursor = self.cursor.next
        if self.cursor == self.tail:
            self.cursor = self.head.next


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
