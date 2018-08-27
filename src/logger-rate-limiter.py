import math


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__window = 10
        self.__map = dict()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        lastTime = self.__map[message] if message in self.__map else -math.inf
        if timestamp - lastTime < self.__window:
            return False
        self.__map[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
