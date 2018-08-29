class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head = ListNode(None)
        self.__tail = ListNode(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.__size:
            return -1
        node = self.__head
        i = 0
        while i <= index and node:
            node = node.next
            i += 1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(self.__size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.__size or index < 0:
            return
        self.__size += 1
        node = self.__head
        i = 0
        while i <= index and node:
            node = node.next
            i += 1
        newNode = ListNode(val)
        newNode.prev = node.prev
        newNode.next = node
        newNode.prev.next = newNode
        newNode.next.prev = newNode

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.__size:
            return
        self.__size -= 1
        node = self.__head
        i = 0
        while i <= index and node:
            node = node.next
            i += 1
        node.prev.next = node.next
        node.next.prev = node.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
