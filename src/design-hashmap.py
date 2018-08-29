class MyHashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__bufLen = 999983  # 99877
        self.__buf = [None for i in range(self.__bufLen)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        idx = self.__getIdx(key)
        node = self.__buf[idx]
        if not node:
            node = MyHashNode(None, None)
            self.__buf[idx] = node
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next.value = value
        else:
            node.next = MyHashNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        node = self.__buf[self.__getIdx(key)]
        if not node:
            return -1
        while node and node.key != key:
            node = node.next
        return node.value if node else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        node = self.__buf[self.__getIdx(key)]
        if not node:
            return
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next = node.next.next

    def __getIdx(self, key):
        return key % self.__bufLen


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

map = MyHashMap()
map.remove(14)
map.get(4)
map.put(7, 3)
map.put(11, 1)
map.put(12, 1)
map.get(7)
map.put(1, 19)
map.put(0, 3)
map.put(1, 8)
map.put(2, 6)
