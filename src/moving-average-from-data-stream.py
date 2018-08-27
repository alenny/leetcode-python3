class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__list = []
        self.__sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__list) >= self.__size:
            self.__sum -= self.__list[-self.__size]
        self.__sum += val
        self.__list.append(val)
        return self.__sum / min(self.__size, len(self.__list))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
