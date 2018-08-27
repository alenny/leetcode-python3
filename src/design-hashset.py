import math


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__bufSize = 9973
        self.__subSize = 101
        self.__buf = [[False for j in range(self.__subSize)]
                      for i in range(self.__bufSize)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.__buf[self.__hash(key)][self.__subIdx(key)] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.__buf[self.__hash(key)][self.__subIdx(key)] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.__buf[self.__hash(key)][self.__subIdx(key)]

    def __hash(self, key):
        return key % self.__bufSize

    def __subIdx(self, key):
        return int(key / self.__bufSize)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
