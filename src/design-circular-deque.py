class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.q = [0 for i in range(k)]
        self.head = 0
        self.tail = -1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            return self.insertLast(value)
        self.head = self.head - 1 if self.head > 0 else len(self.q) - 1
        self.q[self.head] = value
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail = self.tail + 1 if self.tail < len(self.q) - 1 else 0
        self.q[self.tail] = value
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = 0
            self.tail = -1
        else:
            self.head = self.head + 1 if self.head < len(self.q) - 1 else 0
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = 0
            self.tail = -1
        else:
            self.tail = self.tail - 1 if self.tail > 0 else len(self.q) - 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.q[self.head]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.q[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.head == 0 and self.tail == -1

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.head == 0 and self.tail == len(self.q) - 1 or self.head > 0 and self.tail == self.head - 1


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

sol = MyCircularDeque(4)
ret = sol.insertFront(9)
ret = sol.deleteLast()
ret = sol.getRear()
ret = sol.getFront()
print(ret)
